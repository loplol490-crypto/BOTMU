from telegram import Update
from telegram.ext import ContextTypes
from keyboards.language_keyboard import language_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    lang = context.user_data.get("lang")

    # если язык ещё не выбран
    if not lang:
        await update.message.reply_text(
            "👋 Привет! Я твой AI-друг и гид по Кыргызстану 🇰🇬\n\n"
            "Сначала выбери язык 👇",
            reply_markup=language_keyboard()
        )
        return

    # если язык уже есть
    await update.message.reply_text(
        "👋 С возвращением!\n\n"
        "Я твой AI-друг по Кыргызстану 🇰🇬\n"
        "Напиши мне что хочешь узнать или напиши 'меню' чтобы открыть кнопки"
    )
