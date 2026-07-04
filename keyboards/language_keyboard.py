from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def language_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
            InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
        ],
        [
            InlineKeyboardButton("🇰🇬 Кыргызча", callback_data="lang_kg"),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
