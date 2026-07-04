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


# обработка кнопок
async def handle_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "lang_ru":
        await query.edit_message_text("Ты выбрал 🇷🇺 Русский")
    elif data == "lang_en":
        await query.edit_message_text("You selected 🇬🇧 English")
    elif data == "lang_kg":
        await query.edit_message_text("Сиз 🇰🇬 Кыргыз тилин тандадыңыз")


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_language))

    app.run_polling()


if __name__ == "__main__":
    main()
