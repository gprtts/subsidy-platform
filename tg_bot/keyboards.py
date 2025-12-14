from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

# стартовое меню
main_kb = ReplyKeyboardMarkup(
    [
        ["📋 Программы"],
        ["🔔 Алерты"],
    ],
    resize_keyboard=True
)

alerts_kb = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("✅ Включить алерты", callback_data="alerts_on"),
            InlineKeyboardButton("❌ Выключить", callback_data="alerts_off"),
        ]
    ]
)
business_kb = ReplyKeyboardMarkup(
    [
        ["ИП", "ООО"],
        ["Самозанятый"],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

region_kb = ReplyKeyboardMarkup(
    [
        ["Москва", "МО"],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

industry_kb = ReplyKeyboardMarkup(
    [
        ["IT", "Торговля"],
        ["Услуги", "Производство"],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
upgrade_kb = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔓 Купить PRO", callback_data="buy_pro")]]
)