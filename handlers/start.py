from aiogram import Router, F, types
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession

from database import Database
from keyboards import get_main_menu_keyboards, get_period_keyboard

start_router = Router()

# 1. Текст выносим в константу наверх файла, чтобы он был доступен везде
WELCOME_TEXT = (
    "📌 <b>Добро пожаловать! Начните пользоваться защищённой связью.</b>\n\n"
    "Попробуй бесплатно, нажми <b>ДЕМО-доступ</b>.\n"
    "Наш сервис обеспечивает полную конфиденциальность вашего трафика.\n\n"
    "🤖 Claude, ChatGPT и другие ИИ из любой локации\n"
    "🍿 Верните себе YouTube в 4K и Instagram без зависаний!\n"
    "🎮 Играй в любые игры\n"
    "Никаких замедлений — только чистый и свободный интернет.\n\n"
    "🎁 <i>Нажмите ДЕМО-доступ для теста или оформите подписку.</i>"
)


# 1. При команде /start — добавляем в БД и шлем новое сообщение с главным меню
@start_router.message(CommandStart())
async def cmd_start(message: types.Message, session: AsyncSession):
    db = Database(session)
    await db.add_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        full_name=message.from_user.full_name
    )

    await message.answer(
        text=WELCOME_TEXT,
        reply_markup=get_main_menu_keyboards(),
        parse_mode="HTML"
    )


# 2. При клике на "Назад" (back_to_main) — просто редактируем существующее сообщение обратно
@start_router.callback_query(F.data == "back_to_main")
async def process_back_to_main(callback: types.CallbackQuery):
    await callback.answer()
    
    await callback.message.edit_text(
        text=WELCOME_TEXT,
        reply_markup=get_main_menu_keyboards(),
        parse_mode="HTML"
    )    