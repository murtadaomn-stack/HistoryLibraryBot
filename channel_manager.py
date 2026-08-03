
import asyncio

from managers.telegram_client import connect
from managers.scanner import scan_books


async def main():

    client = await connect()

    books = await scan_books(client)

    print()

    print("تم العثور على", len(books), "كتابًا")


asyncio.run(main())
