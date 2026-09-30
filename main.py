import asyncio
import logging
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.dispatcher.middlewares.base import BaseMiddleware

# Импортируем engine, фабрику сессий и Base из database.py
from database import engine, async_session
from models import Base
from handlers.start import start_router
from handlers.buy import buy_router

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    exit("Ошибка: Токен бота не найден в файле .env!")
else:
    print("Token is safe")


# -------------------------------------------------------------
# Middleware: создает и прокидывает session в каждый хэндлер , 
#этот нужен для фильтрации сообщение
# как фильт с крышками с двух сторон, без него пришлось бы в каждом handlers писать вручную,
# если где то забыть написать то база осталась бы открытой
# -------------------------------------------------------------
class DbSessionMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        async with async_session() as session:
            data["session"] = session  # Передаем session в хэндлеры
            return await handler(event, data)


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # Регистрируем Middleware для работы с сессиями, включатель фильтра
    dp.update.middleware(DbSessionMiddleware())

    # Подключаем роутеры
    dp.include_routers(
        start_router, 
        buy_router

        )

    # 1. Создаём таблицы в БД
    print("Проверяем и создаем таблицы в базе данных...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Таблицы успешно готовы к работе!")

    # 2. Запуск бота
    try:
        print("Бот запущен...")
        await dp.start_polling(bot)
    finally:
        await engine.dispose()
        print("Соединение с БД закрыто.")


if __name__ == "__main__":
    print("Bot working...")
    asyncio.run(main())
