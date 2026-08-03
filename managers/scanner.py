import os

from dotenv import load_dotenv

load_dotenv()

CHANNEL = os.getenv("CHANNEL")


async def scan_books(client):

    books = []

    total = 0

    async for message in client.iter_messages(CHANNEL):

        if not message.document:
            continue

        if message.document.mime_type != "application/pdf":
            continue

        total += 1

        name = "Unknown.pdf"

        for attr in message.document.attributes:

            if hasattr(attr, "file_name"):
                name = attr.file_name

        books.append(
            {
                "message_id": message.id,
                "name": name,
                "size": message.document.size,
            }
        )

        print(f"{total} - {name}")

    print()

    print("عدد الكتب:", total)

    return books
