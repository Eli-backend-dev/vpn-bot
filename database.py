#database.py — это повар на кухне (берём ингредиенты, выпекаем, достаем из печи).

import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from urllib.parse import quote_plus
from sqlalchemy import select
from datetime import datetime, timezone

from models import Base, User, Order


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





    async def create_order(self, user_id: int, period_code: str, amount: int) -> Order:
        """Создает новый заказ со статусом 'pending'"""
        order = Order(
            user_id=user_id,
            period_code=period_code, #  order = товар кола бургер
            amount=amount,
            status="pending"
        )
        self.session.add(order)  # Заказ формируется и ждёт оплаты
        await self.session.commit() # «Готовьте! Заказ официальный!». И на экране загорается номер: Заказ №45.
        await self.session.refresh(order) #
        return order #

    # 2. Получение заказа по его ID
    async def get_order(self, order_id: int) -> Order | None:
        """Находит заказ по его уникальному номеру"""
        result = await self.session.execute(
            select(Order).where(Order.id == order_id)
        )
        return result.scalar_one_or_none()

    # 3. Отметка заказа как оплаченного
    async def mark_order_as_paid(self, order_id: int) -> bool:
        """Меняет статус заказа на 'paid' и фиксирует время оплаты"""
        order = await self.get_order(order_id)
        if order and order.status == "pending":
            order.status = "paid"
            order.paid_at = datetime.now(timezone.utc)
            await self.session.commit()
            return True
        return False

    # 4. Получение всей истории заказов пользователя
    async def get_user_orders(self, user_id: int) -> list[Order]:
        """Возвращает список всех заказов пользователя от новых к старым"""
        result = await self.session.execute(
            select(Order)
            .where(Order.user_id == user_id)
            .order_by(Order.created_at.desc())
        )
        return list(result.scalars().all())            

    