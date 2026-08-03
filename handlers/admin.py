from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import ContextTypes


async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [

        [
            InlineKeyboardButton(
                "📚 فحص القناة",
                callback_data="scan"
            )
        ],

        [
            InlineKeyboardButton(
                "📖 الكتب المكررة",
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
        ],

        [
            InlineKeyboardButton(
                "⛔ إيقاف العملية",
                callback_data="cancel"
            )
        ]

    ]

    await update.message.reply_text(
        "📚 لوحة إدارة المكتبة",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
