from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import ContextTypes


async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [

        [
            InlineKeyboardButton(
                "📥 فحص القناة",
                callback_data="scan"
            )
        ],

        [
            InlineKeyboardButton(
                "📚 جميع الكتب",
                callback_data="books"
            )
        ],

        [
            InlineKeyboardButton(
                "🔍 البحث",
                callback_data="search"
            )
        ],

        [
            InlineKeyboardButton(
                "♻️ الكتب المكررة",
                callback_data="duplicates"
            )
        ],

        [
            InlineKeyboardButton(
                "🗑 حذف المكرر",
                callback_data="clean"
            )
        ],

        [
            InlineKeyboardButton(
                "📊 الإحصائيات",
                callback_data="stats"
            )
        ],

        [
            InlineKeyboardButton(
                "🔄 إعادة الفهرسة",
                callback_data="reindex"
            )
        ]

    ]

    await update.message.reply_text(
        "📚 لوحة إدارة History Library AI",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def admin_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    if query.data == "scan":

        await query.edit_message_text(
            "📥 سيتم تشغيل فحص القناة قريباً..."
        )

    elif query.data == "books":

        await query.edit_message_text(
            "📚 سيتم عرض جميع الكتب..."
        )

    elif query.data == "search":

        await query.edit_message_text(
            "🔍 اكتب:\n/search اسم الكتاب"
        )

    elif query.data == "duplicates":

        await query.edit_message_text(
            "♻️ جاري فحص الكتب المكررة..."
        )

    elif query.data == "clean":

        keyboard = [
            [
                InlineKeyboardButton(
                    "✅ نعم",
                    callback_data="confirm_clean"
                ),
                InlineKeyboardButton(
                    "❌ لا",
                    callback_data="cancel_clean"
                )
            ]
        ]

        await query.edit_message_text(
            "⚠️ هل تريد حذف جميع الكتب المكررة؟",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "confirm_clean":

        await query.edit_message_text(
            "🗑 سيتم حذف الكتب المكررة...\n(سنربطها لاحقاً مع Telethon)"
        )

    elif query.data == "cancel_clean":

        await query.edit_message_text(
            "❌ تم إلغاء العملية."
        )

    elif query.data == "stats":

        await query.edit_message_text(
            "📊 جاري استخراج الإحصائيات..."
        )

    elif query.data == "reindex":

        await query.edit_message_text(
            "🔄 سيتم إعادة فهرسة المكتبة..."
        )
