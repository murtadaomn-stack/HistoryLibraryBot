import sqlite3

from telegram import Update
from telegram.ext import ContextTypes

DB_PATH = "data/books.db"


async def list_books(update: Update, context: ContextTypes.DEFAULT_TYPE):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title,pages
        FROM books
        ORDER BY id DESC
        LIMIT 20
    """)

    rows = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM books")

    total = cursor.fetchone()[0]

    conn.close()

    if not rows:

        await update.effective_message.reply_text(
            "لا توجد كتب داخل المكتبة."
        )

        return

    text = f"📚 عدد الكتب: {total}\n\n"

    for i, row in enumerate(rows, start=1):

        text += f"{i}- {row[0]}\n"

        text += f"📄 الصفحات: {row[1]}\n\n"

    await update.effective_message.reply_text(text)
