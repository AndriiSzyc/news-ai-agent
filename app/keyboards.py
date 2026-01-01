from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def open_news_keyboard(news_id: int):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Відкрити новину",
                    callback_data=f"open:{news_id}"
                    )
            ]
        ]
    )


def back_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Назад",
                    callback_data="back"
                    )
            ]
        ]
    )