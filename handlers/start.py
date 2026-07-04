from telegram import Update
from telegram.ext import ContextTypes
from keyboards.language_keyboard import language_keyboard
from keyboards.menu import main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    lang = context.user_data.get("lang")

    # если язык не выбран → выбор языка
    if not lang:
        await update.message.reply_text(
            "Выбери язык 👇",
            reply_markup=language_keyboard()
        )
        return

    # если язык есть → показываем меню
    await update.message.reply_text(
        "Главное меню 👇",
        reply_markup=main_menu()
    )
