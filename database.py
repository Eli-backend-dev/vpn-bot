#database.py — это повар на кухне (берём ингредиенты, выпекаем, достаем из печи).

import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from urllib.parse import quote_plus
from sqlalchemy import select

from models import Base, User


load_dotenv()
user = os.getenv("DB_USER")
password = quote_plus(os.getenv("DB_PASSWORD"))
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
DATABASE_URL = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)





class Database:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_user(self, user_id: int, username: str, full_name: str):
        # 1. Проверяем, есть ли уже такой юзер
        query = select(User).where(User.user_id == user_id)
        result = await self.session.execute(query)
        user = result.scalar_one_or_none()

        # 2. Если пользователя нет — создаем объект и сохраняем
        if not user:
        #   ИМЯ_ПАРАМЕТРА = ЗНАЧЕНИЕ
            new_user = User(
                user_id=user_id,
                username=username,
                full_name=full_name
            )
            self.session.add(new_user)
            await self.session.commit() # Сохраняет данные в БД    

    