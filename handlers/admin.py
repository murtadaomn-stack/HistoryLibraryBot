from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from telegram.ext import ContextTypes

import asyncio

from channel_manager import scan_channel
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

        msg = await query.edit_message_text(
            "📥 بدأ فحص القناة...\n\n⏳ يرجى الانتظار..."
        )

        asyncio.create_task(
            scan_channel(
                bot=context.bot,
                chat_id=query.message.chat_id,
                message_id=msg.message_id,
            )
        )

        return

    elif query.data == "all_books":

        await list_books(update, context)
        return

    elif query.data == "duplicates":

        await query.edit_message_text(
            "🔍 جاري فحص الكتب المكررة..."
        )

        return

    elif query.data == "delete_duplicates":

        keyboard = [
            [
                InlineKeyboardButton(
                    "✅ نعم",
                    callback_data="confirm_delete",
                ),
                InlineKeyboardButton(
                    "❌ إلغاء",
                    callback_data="cancel_delete",
                ),
            ]
        ]

        await query.edit_message_text(
            "⚠️ هل تريد حذف جميع الكتب المكررة؟",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

        return

    elif query.data == "confirm_delete":

        await query.edit_message_text(
            "🗑 جاري حذف الكتب المكررة..."
        )

        return

    elif query.data == "cancel_delete":

        await query.edit_message_text(
            "❌ تم إلغاء العملية."
        )

        return

    elif query.data == "stats":

        await query.edit_message_text(
            "📊 سيتم عرض الإحصائيات قريبًا."
        )

        return

    elif query.data == "reindex":

        msg = await query.edit_message_text(
            "🔄 بدأت إعادة الفهرسة...\n\n⏳ يرجى الانتظار..."
        )

        asyncio.create_task(
            scan_channel(
                bot=context.bot,
                chat_id=query.message.chat_id,
                message_id=msg.message_id,
            )
        )

        return

    else:

        await query.edit_message_text(
            "❓ أمر غير معروف."
        )
