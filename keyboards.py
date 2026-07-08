from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⭐ نقاطي"), KeyboardButton(text="🎟️ بطاقات السحب")],
        [KeyboardButton(text="📋 المهام"), KeyboardButton(text="🎁 المسابقات")],
        [KeyboardButton(text="🏆 المتصدرون"), KeyboardButton(text="👥 دعوة صديق")],
        [KeyboardButton(text="📜 القوانين"), KeyboardButton(text="📞 الدعم")],
    ],
    resize_keyboard=True
)
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def task_keyboard(task_id, url):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔗 فتح المهمة",
                    url=url
                )
            ],
            [
                InlineKeyboardButton(
                    text="✅ أكملت المهمة",
                    callback_data=f"complete_{task_id}"
                )
            ]
        ]
    )

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ أكملت المهمة",
                    callback_data=f"complete_{task_id}"
                )
            ]
        ]
    )
