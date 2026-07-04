from telegram import Update
from telegram.ext import ContextTypes
from keyboards.language_keyboard import language_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    lang = context.user_data.get("lang")

    if lang == "ru":
        text = "Привет 👋 Ты уже выбрал русский язык"
    elif lang == "en":
        text = "Hello 👋 You already selected English"
    elif lang == "kg":
        text = "Салам 👋 Сен кыргыз тилин тандагансың"
    else:
        text = "Выбери язык 👇"

    await update.message.reply_text(
        text,
        reply_markup=language_keyboard()
    )
