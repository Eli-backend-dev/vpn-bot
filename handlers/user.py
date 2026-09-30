from aiogram import Router, F, types
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession

from database import Database
from keyboards import get_main_inline_kb

users_router = Router()

@users_router.message(CommandStart())
async def cmd_start(message: types.Message, session: AsyncSession):

    db = Database(session)

    await db.add_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        full_name=message.from_user.full_name
    )
    
    await message.answer("👤 Личный кабинет\n\nРады видеть тебя!",
    reply_markup=get_main_inline_kb()
    )