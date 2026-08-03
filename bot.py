import os
import asyncio

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

from config import BOT_TOKEN
from database import init_db

from handlers.start import start
from handlers.pdf import pdf_handler
from handlers.search import search
from handlers.admin import admin, admin_buttons


def main():

    if not BOT_TOKEN:
        raise Exception("BOT_TOKEN is not set")

    asyncio.set_event_loop(asyncio.new_event_loop())

    os.makedirs("books", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    os.makedirs("temp", exist_ok=True)

    init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    # ==========================
    # Commands
    # ==========================

    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    app.add_handler(
        CommandHandler(
            "search",
            search
        )
    )

    app.add_handler(
        CommandHandler(
            "admin",
            admin
        )
    )

    # ==========================
    # PDF Upload
    # ==========================

    app.add_handler(
        MessageHandler(
            filters.Document.PDF,
            pdf_handler,
        )
    )

    # ==========================
    # Inline Buttons
    # ==========================

    app.add_handler(
        CallbackQueryHandler(
            admin_buttons
        )
    )

    print("===================================")
    print("📚 History Library AI Started")
    print("===================================")

    app.run_polling(close_loop=False)


if __name__ == "__main__":
    main()
