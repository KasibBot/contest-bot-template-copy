from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⭐ نقاطي"),
            KeyboardButton(text="📋 المهام")
        ],
        [
            KeyboardButton(text="🎟️ بطاقات السحب"),
            KeyboardButton(text="🎁 المسابقات")
        ],
        [
            KeyboardButton(text="👥 دعوة صديق"),
            KeyboardButton(text="🏆 المتصدرون")
        ],
        [
            KeyboardButton(text="📜 القوانين"),
            KeyboardButton(text="📞 الدعم")
        ]
    ],
    resize_keyboard=True
)


def task_keyboard(task_id, url):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔗 فتح المهمة",
                    url=url
                )
            ]
        ]
    )


def task_keyboard(task_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔗 فتح المهمة",
                    callback_data=f"open_{task_id}"
                )
            ]
        ]
    )
