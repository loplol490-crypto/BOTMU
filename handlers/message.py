from telegram import Update
from telegram.ext import ContextTypes
from services.ai import get_ai_response


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_id = update.effective_user.id

    response = await get_ai_response(user_text, user_id)

    await update.message.reply_text(response)
