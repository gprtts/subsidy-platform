import os
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

from core.settings import TELEGRAM_TOKEN
from tg_bot.handlers import (
    start,
    set_business,
    set_region,
    set_industry,
    programs,
    alerts_menu,
    alerts_callback,
    buy_pro,
)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Regex("^(ИП|ООО|Самозанятый)$"), set_business))
app.add_handler(MessageHandler(filters.Regex("^(Москва|МО)$"), set_region))
app.add_handler(MessageHandler(filters.Regex("^(IT|Торговля|Услуги|Производство)$"), set_industry))
app.add_handler(MessageHandler(filters.Regex("^📋 Программы$"), programs))
app.add_handler(MessageHandler(filters.Regex("^🔔 Алерты$"), alerts_menu))

app.add_handler(CallbackQueryHandler(alerts_callback, pattern="^alerts_"))
app.add_handler(CallbackQueryHandler(buy_pro, pattern="^buy_pro"))

print("🤖 Telegram bot started")
app.run_polling()
