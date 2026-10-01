#models.py — это рецепт пиццы (список ингредиентов: тесто, сыр, соус).

from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey
from datetime import datetime, timezone

class Base(DeclarativeBase):
    pass

# Описываем таблицу "users"
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True) # Порядковый номер
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True) # Telegram ID
    username: Mapped[str | None] = mapped_column(String(255))
    full_name: Mapped[str | None] = mapped_column(String(255))
    
    
    
    
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    period_code = Column(String, nullable=False) # buy_period_1m
    amount = Column(Integer, nullable=False)     # 150
    status = Column(String, default="pending")   # pending / paid / canceled
    created_at = Column(
        DateTime(timezone=True), 
        default=lambda: datetime.now(timezone.utc)
    )

# надо закончить логику в базе данных   об истории и сохранение заказов 