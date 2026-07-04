from config import BOT_TOKEN
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

from handlers.start import start
from keyboards.language_keyboard import language_keyboard
from keyboards.menu import main_menu


# обработка выбора языка
async def handle_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "lang_ru":
        context.user_data["lang"] = "ru"
        await query.edit_message_text("Ты выбрал 🇷🇺 Русский")

    elif data == "lang_en":
        context.user_data["lang"] = "en"
        await query.edit_message_text("You selected 🇬🇧 English")

    elif data == "lang_kg":
        context.user_data["lang"] = "kg"
        await query.edit_message_text("Сиз 🇰🇬 Кыргыз тилин тандадыңыз")


# обработка меню
async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "guide":
        await query.edit_message_text("🗺 Гид по Кыргызстану")
    elif data == "food":
        await query.edit_message_text("🍜 Еда Кыргызстана")
    elif data == "transport":
        await query.edit_message_text("🚌 Транспорт Кыргызстана")
    elif data == "settings":
        await query.edit_message_text("⚙️ Настройки")


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    # сначала язык
    app.add_handler(CallbackQueryHandler(handle_language))

    # потом меню
    app.add_handler(CallbackQueryHandler(handle_menu))

    app.run_polling()


if __name__ == "__main__":
    main()
