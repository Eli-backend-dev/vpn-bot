#models.py — это рецепт пиццы (список ингредиентов: тесто, сыр, соус).

from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column
from sqlalchemy import BigInteger, String

class Base(DeclarativeBase):
    pass

# Описываем таблицу "users"
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True) # Порядковый номер
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True) # Telegram ID
    username: Mapped[str | None] = mapped_column(String(255))
    full_name: Mapped[str | None] = mapped_column(String(255))
