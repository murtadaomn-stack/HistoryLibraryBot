from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📚 أهلاً بك في History Library AI\n\n"
        "🤖 البوت يعمل بنجاح.\n\n"
        "أرسل أي كتاب PDF وسأقوم بفحصه."
    )

    await update.message.reply_text(text)
