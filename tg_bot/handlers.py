from telegram import Update
from telegram.ext import ContextTypes

from db.connection import get_connection
from tg_bot.access import check_access, consume_request
from tg_bot.keyboards import (
    main_kb,
    business_kb,
    region_kb,
    industry_kb,
    upgrade_kb,
)

from payments.service import create_pro_subscription


# =========================
# helpers
# =========================

def create_user(tg_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO users (tg_id)
        VALUES (%s)
        ON CONFLICT (tg_id) DO NOTHING
        """,
        (tg_id,),
    )
    conn.commit()
    conn.close()


def get_user(tg_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT tg_id, business, region, industry, free_requests FROM users WHERE tg_id = %s",
        (tg_id,),
    )
    row = cur.fetchone()
    conn.close()
    return row


# =========================
# base flow
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_id = update.effective_user.id
    create_user(tg_id)

    await update.message.reply_text(
        "Привет 👋\n\n"
        "Я помогу найти актуальные субсидии и гранты под твой бизнес.\n\n"
        "Для начала выбери форму бизнеса:",
        reply_markup=business_kb,
    )


async def set_business(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_id = update.effective_user.id
    business = update.message.text

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET business = %s WHERE tg_id = %s",
        (business, tg_id),
    )
    conn.commit()
    conn.close()

    await update.message.reply_text(
        "Выбери регион:",
        reply_markup=region_kb,
    )


async def set_region(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_id = update.effective_user.id
    region = update.message.text

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET region = %s WHERE tg_id = %s",
        (region, tg_id),
    )
    conn.commit()
    conn.close()

    await update.message.reply_text(
        "Теперь выбери отрасль:",
        reply_markup=industry_kb,
    )


async def set_industry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_id = update.effective_user.id
    industry = update.message.text

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET industry = %s WHERE tg_id = %s",
        (industry, tg_id),
    )
    conn.commit()
    conn.close()

    await update.message.reply_text(
        "Готово ✅\n\nНажми «📋 Программы», чтобы посмотреть подходящие меры поддержки.",
        reply_markup=main_kb,
    )


# =========================
# programs
# =========================

async def programs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_id = update.effective_user.id

    allowed, msg = check_access(tg_id)
    if not allowed:
        await update.message.reply_text(
            msg,
            reply_markup=upgrade_kb,
        )
        return

    consume_request(tg_id)

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT title, description
        FROM programs
        ORDER BY id DESC
        LIMIT 5
        """
    )
    rows = cur.fetchall()
    conn.close()

    if not rows:
        await update.message.reply_text("Пока нет программ под твои фильтры 😔")
        return

    for title, desc in rows:
        await update.message.reply_text(
            f"🏛 {title}\n\n{desc}"
        )


# =========================
# alerts
# =========================

async def alerts_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    tg_id = query.from_user.id

    conn = get_connection()
    cur = conn.cursor()

    if query.data == "alerts_on":
        cur.execute(
            "UPDATE users SET alerts_enabled = TRUE WHERE tg_id = %s",
            (tg_id,),
        )
        msg = "✅ Уведомления включены"

    elif query.data == "alerts_off":
        cur.execute(
            "UPDATE users SET alerts_enabled = FALSE WHERE tg_id = %s",
            (tg_id,),
        )
        msg = "❌ Уведомления выключены"

    conn.commit()
    conn.close()

    await query.answer()
    await query.message.reply_text(msg)


async def alerts_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔔 Управление уведомлениями:",
        reply_markup=alerts_kb,
    )


# =========================
# payments / pro
# =========================

async def upgrade_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    tg_id = query.from_user.id

    payment = create_pro_subscription(tg_id)

    await query.answer()
    await query.message.reply_text(
        "💎 PRO-доступ\n\n"
        "Безлимитные запросы\n"
        "Алерты о новых субсидиях\n\n"
        f"👉 Оплата: {payment['pay_url']}"
    )
