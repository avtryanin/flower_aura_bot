from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers import admin, client
from middlewares import DatabaseSessionMiddleware, ErrorLoggingMiddleware


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot=bot)

    dp.message.middleware(DatabaseSessionMiddleware())
    dp.callback_query.middleware(DatabaseSessionMiddleware())
    dp.update.middleware(ErrorLoggingMiddleware())

    dp.include_router(admin.router)
    dp.include_router(client.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
