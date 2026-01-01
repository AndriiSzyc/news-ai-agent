import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import router

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start_bot():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Підключаємо логіку реакцій
    dp.include_router(router)
    
    # Запускаємо бота
    await dp.start_polling(bot)