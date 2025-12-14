import os
from dotenv import load_dotenv

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

from tg_bot.handlers import (
    start,
    set_business,
    set_region,
    set_industry,
    programs,
    alerts_callback,
    upgrade_callback,
)

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

# commands
app.add_handler(CommandHandler("start", start))

# text buttons
app.add_handler(MessageHandler(filters.Regex("^(ИП|ООО|Самозанятый)$"), set_business))
app.add_handler(MessageHandler(filters.Regex("^(Москва|МО)$"), set_region))
app.add_handler(MessageHandler(filters.Regex("^(IT|Торговля|Услуги|Производство)$"), set_industry))
app.add_handler(MessageHandler(filters.Regex("^📋 Программы$"), programs))

# inline callbacks
app.add_handler(CallbackQueryHandler(alerts_callback, pattern="^alerts_"))
app.add_handler(CallbackQueryHandler(upgrade_callback, pattern="^upgrade$"))

print("🤖 Bot started")
app.run_polling()
