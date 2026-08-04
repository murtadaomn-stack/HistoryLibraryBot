from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import ContextTypes
from handlers.books import list_books

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "📥 فحص القناة",
                callback_data="scan_channel",
            )
        ],
        [
            InlineKeyboardButton(
                "📚 جميع الكتب",
                callback_data="all_books",
            )
        ],
        [
            InlineKeyboardButton(
                "🔍 فحص المكرر",
                callback_data="duplicates",
            )
        ],
        [
            InlineKeyboardButton(
                "🗑 حذف المكرر",
                callback_data="delete_duplicates",
            )
        ],
        [
            InlineKeyboardButton(
                "📊 الإحصائيات",
                callback_data="stats",
            )
        ],
        [
            InlineKeyboardButton(
                "🔄 إعادة الفهرسة",
                callback_data="reindex",
            )
        ],
    ]

    await update.message.reply_text(
        "📚 لوحة إدارة History Library AI",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def admin_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "scan_channel":
        await query.edit_message_text(
            "📥 سيتم قريباً بدء فحص القناة..."
        )

    elif query.data == "all_books":
        await list_books(update, context)
        return

    elif query.data == "duplicates":
        await query.edit_message_text(
            "🔍 سيتم قريباً فحص الكتب المكررة..."
        )

    elif query.data == "delete_duplicates":
        await query.edit_message_text(
            "🗑 سيتم قريباً حذف الكتب المكررة..."
        )

    elif query.data == "stats":
        await query.edit_message_text(
            "📊 سيتم قريباً عرض الإحصائيات..."
        )

    elif query.data == "reindex":
        await query.edit_message_text(
            "🔄 سيتم قريباً إعادة فهرسة القناة..."
        )
