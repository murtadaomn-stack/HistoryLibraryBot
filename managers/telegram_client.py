import os

from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
PHONE = os.getenv("PHONE")

# إنشاء مجلد sessions إذا لم يكن موجودًا
os.makedirs("sessions", exist_ok=True)

client = TelegramClient(
    "sessions/history_library",
    API_ID,
    API_HASH
)

async def connect():
    await client.start(phone=PHONE)
    return client
