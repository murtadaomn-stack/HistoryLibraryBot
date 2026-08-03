import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))

API_HASH = os.getenv("API_HASH")

PHONE = os.getenv("PHONE")

CHANNEL = os.getenv("CHANNEL")

BOT_TOKEN = os.getenv("BOT_TOKEN")

DB_PATH = "data/books.db"

TEMP_PATH = "temp"

BOOKS_PATH = "books"

REPORT_PATH = "reports"

SESSION = "sessions/history_library"
