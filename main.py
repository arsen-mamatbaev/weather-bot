import os
import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from core.config import settings
from core.handlers.users import start

bot = Bot(settings.bot.token)
dp = Dispatcher()


async def main():
    dp.message.register(start, CommandStart())
    
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
