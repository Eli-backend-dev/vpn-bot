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

    id = Column(Integer, primary_key=True, autoincrement=True) # Создай столбец id, храни там целые числа, сделай его уникальным номером записи и сам автоматически увеличивай его на +1 для каждого нового заказа
    user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False) # Создай столбец user_id для больших чисел, обязательно свяжи его с таблицей пользователей и не разрешай создавать заказ без указания пользователя
    period_code = Column(String, nullable=False) # Создай текстовый столбец period_code, в который обязательно нужно записывать код выбранного периода подписки
    amount = Column(Integer, nullable=False)     # Создай столбец amount для целых чисел, в который обязательно нужно записывать итоговую стоимость заказа в рублях
    status = Column(String, default="pending")   # pending / paid / canceled Создай текстовый столбец status, и при создании каждого нового заказа автоматически записывай туда слово "pending" (ожидает оплаты)
    created_at = Column(
        DateTime(timezone=True), 
        default=lambda: datetime.now(timezone.utc)
    )# В ней фиксируется точный момент, когда пользователь нажал кнопку «Купить» и сформировал счёт.
    paid_at = Column(DateTime(timezone=True), nullable=True) # время когда получили оплату




# 