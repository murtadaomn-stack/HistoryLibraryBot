import sqlite3

from telegram import Update
from telegram.ext import ContextTypes

DB_PATH = "data/books.db"


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "استخدم الأمر بهذا الشكل:\n\n/search كلمة"
        )
        return

    keyword = " ".join(context.args)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT title,pages
        FROM books
        WHERE full_text LIKE ?
        LIMIT 10
        """,
        (f"%{keyword}%",),
    )

    rows = cursor.fetchall()

    conn.close()

    if not rows:
        await update.message.reply_text("❌ لم يتم العثور على أي نتيجة.")
        return

    msg = "📚 نتائج البحث:\n\n"

    for i, row in enumerate(rows, start=1):
        msg += f"{i}. {row[0]}\n"
        msg += f"📄 عدد الصفحات: {row[1]}\n\n"

    await update.message.reply_text(msg)
