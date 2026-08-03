import os
import asyncio

from telegram.ext import Application, CommandHandler

from config import BOT_TOKEN
from database import init_db
from handlers.start import start


def main():
    if not BOT_TOKEN:
        raise Exception("BOT_TOKEN is not set")

    asyncio.set_event_loop(asyncio.new_event_loop())

    os.makedirs("books", exist_ok=True)
    os.makedirs("data", exist_ok=True)

    init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("History Library AI Started")

    app.run_polling(close_loop=False)


if __name__ == "__main__":
    main()
