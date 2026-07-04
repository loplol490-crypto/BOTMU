from telegram import Update
from telegram.ext import ContextTypes
from keyboards.language_keyboard import language_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Выбери язык 👇",
        reply_markup=language_keyboard()
    )
