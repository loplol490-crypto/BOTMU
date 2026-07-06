from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я твой AI-друг и гид по Кыргызстану 🇰🇬\n\n"
        "Я помогу тебе:\n"
        "🏙 Найти интересные места в Бишкеке\n"
        "🌊 Узнать про Иссык-Куль\n"
        "🍜 Посоветовать еду\n"
        "🚌 Подсказать про транспорт\n\n"
        "💬 Просто напиши, например:\n"
        "• что посмотреть в Бишкеке\n"
        "• куда сходить\n"
        "• что поесть\n\n"
        "И я отвечу как живой местный гид 😄"
    )
