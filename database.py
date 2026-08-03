import sqlite3

DB_NAME = "books.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT,
        telegram_file_id TEXT UNIQUE,
        pages INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def add_book(file_name, telegram_file_id, pages):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    INSERT OR IGNORE INTO books(file_name,telegram_file_id,pages)
    VALUES(?,?,?)
    """,(file_name,telegram_file_id,pages))

    conn.commit()
    conn.close()
