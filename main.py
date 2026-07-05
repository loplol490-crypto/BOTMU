from config import BOT_TOKEN
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

from handlers.start import start
from keyboards.menu import main_menu


async def handle_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "lang_ru":
        context.user_data["lang"] = "ru"
        await query.edit_message_text("Главное меню 👇", reply_markup=main_menu())

    elif data == "lang_en":
        context.user_data["lang"] = "en"
        await query.edit_message_text("Main menu 👇", reply_markup=main_menu())

    elif data == "lang_kg":
        context.user_data["lang"] = "kg"
        await query.edit_message_text("Башкы меню 👇", reply_markup=main_menu())

    elif data == "guide":
        await query.edit_message_text("🗺 Гид по Кыргызстану", reply_markup=main_menu())

    elif data == "food":
        await query.edit_message_text("🍜 Еда Кыргызстана", reply_markup=main_menu())

    elif data == "transport":
        await query.edit_message_text("🚌 Транспорт Кыргызстана", reply_markup=main_menu())

    elif data == "settings":
        await query.edit_message_text("⚙️ Настройки", reply_markup=main_menu())


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callbacks))

    app.run_polling()


if __name__ == "__main__":
    main()
