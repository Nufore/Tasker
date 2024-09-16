import asyncio
import logging
from aiogram import Bot, Dispatcher
from routes import router

from config import BOT_TOKEN
from database.connection import async_main

tasker_bot = Bot(token=BOT_TOKEN)


async def main():
    dp = Dispatcher()
    dp.include_router(router)

    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    logging.basicConfig(level=logging.INFO)

    await dp.start_polling(tasker_bot)


async def startup(dispatcher: Dispatcher):
    await async_main()
    print('Starting up...')


async def shutdown(dispatcher: Dispatcher):
    print('Shutting down...')


if __name__ == "__main__":
    asyncio.run(main())

