import logging

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import user
from handlers import admin
load_dotenv()

async def main() -> None:
    bot = Bot(token='BOT_TOKEN', parse_mode="HTML")
    dp = Dispatcher()

    logging.basicConfig(level=logging.INFO)

    dp.include_router(user.router)
    dp.include_router(admin.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)