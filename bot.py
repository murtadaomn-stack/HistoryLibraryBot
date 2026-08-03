import os

from telegram.ext import (
    Application,
        CommandHandler,
        )

        from config import BOT_TOKEN
        from database import init_db
        from handlers.start import start


        def main():

            if not BOT_TOKEN:
                    raise Exception("BOT_TOKEN غير موجود")

                        os.makedirs("books", exist_ok=True)
                            os.makedirs("data", exist_ok=True)

                                init_db()

                                    app = Application.builder().token(BOT_TOKEN).build()

                                        app.add_handler(CommandHandler("start", start))

                                            print("History Library AI Started")

                                                app.run_polling()


                                                if __name__ == "__main__":
                                                    main()