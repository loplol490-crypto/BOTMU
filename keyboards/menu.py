from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():
    keyboard = [
        [InlineKeyboardButton("🗺 Гид по Кыргызстану", callback_data="guide")],
        [InlineKeyboardButton("🍜 Еда", callback_data="food")],
        [InlineKeyboardButton("🚌 Транспорт", callback_data="transport")],
        [InlineKeyboardButton("⚙️ Настройки", callback_data="settings")],
    ]

    return InlineKeyboardMarkup(keyboard)
