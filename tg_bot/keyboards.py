from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


# ===== Main menu =====
main_kb = ReplyKeyboardMarkup(
    [
        ["📋 Программы"],
        ["🔔 Уведомления"],
    ],
    resize_keyboard=True,
)


# ===== Business type =====
business_kb = ReplyKeyboardMarkup(
    [
        ["ИП", "ООО"],
        ["Самозанятый"],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)


# ===== Region =====
region_kb = ReplyKeyboardMarkup(
    [
        ["Москва", "МО"],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)


# ===== Industry =====
industry_kb = ReplyKeyboardMarkup(
    [
        ["IT", "Торговля"],
        ["Услуги", "Производство"],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)


# ===== Alerts inline =====
alerts_kb = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔔 Включить", callback_data="alerts_on"),
            InlineKeyboardButton("🔕 Выключить", callback_data="alerts_off"),
        ]
    ]
)


# ===== Upgrade / PRO =====
upgrade_kb = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("💎 Купить PRO", callback_data="upgrade"),
        ]
    ]
)
