from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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


def complete_keyboard(task_id):
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
