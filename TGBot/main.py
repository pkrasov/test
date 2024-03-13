import asyncio
import config
from aiogram import F, Bot,Dispatcher,types
from aiogram.filters.command import Command
import logging
from handlers import commands
from handlers import ascker


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=config.token)

    dp = Dispatcher()
    dp.include_router(ascker.dp)
    dp.include_router(commands.dp)
   
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

