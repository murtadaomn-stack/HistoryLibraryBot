from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
    📚 History Library AI

    مرحبًا بك.

    أنا مساعد ذكي لإدارة المكتبات.

    يمكنني:

    📖 استقبال الكتب PDF
    🔍 اكتشاف الكتب المكررة
    🗂 تصنيف الكتب
    🤖 استخدام الذكاء الاصطناعي

    الإصدار:
    v1.0
    """

        await update.message.reply_text(text)