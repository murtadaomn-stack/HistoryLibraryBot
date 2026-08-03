import hashlib
import os
import sqlite3

from telegram import Update
from telegram.ext import ContextTypes

from services.pdf_reader import extract_pdf_text, create_summary


DB_PATH = "data/books.db"


async def pdf_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    document = update.message.document

    if document.mime_type != "application/pdf":
        return

    await update.message.reply_text("📥 جاري حفظ الكتاب...")

    file = await context.bot.get_file(document.file_id)

    os.makedirs("books", exist_ok=True)

    file_path = f"books/{document.file_name}"

    await file.download_to_drive(file_path)

    with open(file_path, "rb") as f:
        file_hash = hashlib.md5(f.read()).hexdigest()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM books WHERE file_hash=?",
        (file_hash,),
    )

    if cursor.fetchone():

        conn.close()

        await update.message.reply_text("📚 هذا الكتاب موجود مسبقًا.")

        return

    try:

        text, pages = extract_pdf_text(file_path)

    except Exception:

        conn.close()

        await update.message.reply_text("❌ تعذر قراءة ملف PDF.")

        return

    summary = create_summary(text)
cursor.execute(
    """
    INSERT INTO books
    (
        title,
        file_name,
        file_hash,
        telegram_file_id,
        pages,
        summary,
        full_text,
        message_id
    )

    VALUES (?,?,?,?,?,?,?,?)
    """,
    (
        document.file_name,
        document.file_name,
        file_hash,
        document.file_id,
        pages,
        summary,
        text,
        update.message.message_id,
    ),
)

    conn.commit()
    conn.close()

    await update.message.reply_text(
        f"""✅ تمت إضافة الكتاب بنجاح.

📄 الاسم:
{document.file_name}

📚 الصفحات:
{pages}

📝 ملخص أولي:

{summary[:1200]}
"""
    )
