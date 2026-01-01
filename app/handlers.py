from aiogram import Router
from aiogram.types import CallbackQuery

from keyboards import back_keyboard

router = Router()

@router.callback_query(lambda c: c.data.startswith("open:"))
async def open_news(callback: CallbackQuery):
    news_id = callback.data.split(":")[1]

    text = (
        f"🟡 Короткий перегляд новини #{news_id}\n\n"
        f"Факт: Тут буде короткий опис події.\n"
        f"Джерело: example.com"
    )

    await callback.message.answer(
        text=text,
        reply_markup=back_keyboard()
    )

    await callback.answer()


@router.callback_query(lambda c: c.data == "back")
async def back(callback: CallbackQuery):
    await callback.message.answer(
        text="Повернулись до дайджесту."
    )

    await callback.answer()