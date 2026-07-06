from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я твой AI-друг и гид по Кыргызстану 🇰🇬\n\n"
        "🏙 Могу подсказать места в Бишкеке\n"
        "🌊 Рассказать про Иссык-Куль\n"
        "🍜 Посоветовать еду\n\n"
        "💬 Напиши: что посмотреть в Бишкеке"
    )
