# نقطة تشغيل البوت
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك، البوت يعمل بنجاح.")

def main():
    # ضع توكن البوت هنا مؤقتاً أو استخدم متغيرات البيئة لاحقاً
    TOKEN = "PUT_YOUR_BOT_TOKEN_HERE"
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
