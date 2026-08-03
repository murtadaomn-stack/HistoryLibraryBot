import sqlite3
import os

DB_PATH = "data/books.db"


def init_db():
    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT,
        author TEXT,

        file_name TEXT,
        file_hash TEXT UNIQUE,
        telegram_file_id TEXT,

        pages INTEGER,
        category TEXT,

        summary TEXT,
        full_text TEXT,

        message_id INTEGER,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()
