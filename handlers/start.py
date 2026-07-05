from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я твой AI-друг и гид по Кыргызстану 🇰🇬\n\n"
        "Я могу помочь тебе с:\n"
        "🏙 Бишкек\n"
        "🌊 Иссык-Куль\n"
        "🍜 Еда\n"
        "🚌 Транспорт\n\n"
        "Просто напиши вопрос 😊"
    )
