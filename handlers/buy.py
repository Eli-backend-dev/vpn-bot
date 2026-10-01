from aiogram import Router, F, types
from aiogram.types import Message , CallbackQuery

from keyboards import get_period_keyboard, get_payment_keyboard

buy_router = Router()

TARIFFS = {
    "buy_period_1m": {"name": "1 месяц", "price": 150},
    "buy_period_3m": {"name": "3 месяца", "price": 400},
    "buy_period_1y": {"name": "1 год", "price": 1200},
}

#Нажатие на "Купить подписку" из главного меню
@buy_router.callback_query(F.data == "buy_subscription")
async def process_buy_click(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        text="💳 <b>ВЫБЕРИТЕ ПЕРИОД</b>",
        reply_markup=get_period_keyboard(),
        parse_mode="HTML"
    )


# 2. Обработка выбора конкретного периода (по префиксу buy_period_)
@buy_router.callback_query(F.data.startswith("buy_period_"))
async def process_period_select(callback: CallbackQuery):
    await callback.answer()
    
    period_code = callback.data  # Например, "buy_period_1m"
    tariff = TARIFFS.get(period_code)

    if not tariff:
        return

    text = (
        f"🛒 <b>Ваш заказ:</b>\n\n"
        f"🔹 <b>Тариф:</b> {tariff['name']}\n"
        f"💰 <b>К оплате:</b> {tariff['price']} ₽\n\n"
        f"Выберите удобный способ оплаты ниже:"
    )

    await callback.message.edit_text(
        text=text,
        reply_markup=get_payment_keyboard(period_code),
        parse_mode="HTML"
    )   


    