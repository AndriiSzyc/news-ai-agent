import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import router

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start_bot():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # підключаємо всі обробники
    dp.include_router(router)

    # стартуємо polling (локальний запуск)
    await dp.start_polling(bot)