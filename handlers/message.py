from telegram import Update
from telegram.ext import ContextTypes

from services.ai import get_ai_response


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    response = await get_ai_response(user_message)

    await update.message.reply_text(response)
