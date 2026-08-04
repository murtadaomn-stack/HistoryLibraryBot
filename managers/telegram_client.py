import os

from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

# إنشاء مجلد الجلسات إذا لم يكن موجودًا
os.makedirs("sessions", exist_ok=True)

client = TelegramClient(
    "sessions/history_library",
    API_ID,
    API_HASH
)


async def connect():
    await client.connect()

    if not await client.is_user_authorized():
        raise Exception(
            "Session غير مسجلة. قم بتسجيل الدخول مرة واحدة محليًا ثم ارفع ملف sessions/history_library.session."
        )

    return client
