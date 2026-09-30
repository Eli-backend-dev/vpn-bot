from aiogram import Router, F, types
from aiogram.types import Message 

from keyboards import get_period_keyboard

buy_router = Router()

# В handlers/buy.py:
@buy_router.callback_query(F.data == "buy_subscription")
async def process_buy_click(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        text="💳 <b>ВЫБЕРИТЕ ПЕРИОД</b>",
        reply_markup=get_period_keyboard(),
        parse_mode="HTML"
    )