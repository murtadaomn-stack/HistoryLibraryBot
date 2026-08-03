import os
import csv
import hashlib
import asyncio

from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
PHONE = os.getenv("PHONE")
CHANNEL = os.getenv("CHANNEL")

client = TelegramClient(
    "sessions/history",
    API_ID,
    API_HASH
)


async def sha256_file(message):

    file_path = await message.download_media("temp")

    h = hashlib.sha256()

    with open(file_path, "rb") as f:

        while True:

            chunk = f.read(8192)

            if not chunk:
                break

            h.update(chunk)

    os.remove(file_path)

    return h.hexdigest()


async def scan():

    await client.start(phone=PHONE)

    os.makedirs("reports", exist_ok=True)

    names = {}
    hashes = {}

    duplicates = []

    total = 0

    async for msg in client.iter_messages(CHANNEL):

        if not msg.document:
            continue

        if msg.document.mime_type != "application/pdf":
            continue

        total += 1

        name = ""

        for a in msg.document.attributes:

            if hasattr(a, "file_name"):
                name = a.file_name

        print(total, "-", name)

        if name in names:

            duplicates.append(
                (
                    "NAME",
                    name,
                    msg.id,
                )
            )

        else:

            names[name] = msg.id

        file_hash = await sha256_file(msg)

        if file_hash in hashes:

            duplicates.append(
                (
                    "HASH",
                    name,
                    msg.id,
                )
            )

        else:

            hashes[file_hash] = msg.id

    with open(
        "reports/duplicates.csv",
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as f:

        writer = csv.writer(f)

        writer.writerow(
            [
                "TYPE",
                "NAME",
                "MESSAGE_ID",
            ]
        )

        writer.writerows(duplicates)

    print()

    print("عدد الكتب:", total)

    print("المكررات:", len(duplicates))

    print("تم إنشاء التقرير داخل reports/duplicates.csv")


with client:

    client.loop.run_until_complete(scan())
