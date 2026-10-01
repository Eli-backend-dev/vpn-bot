from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_menu_keyboards() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    
    # Добавляем кнопки. callback_data — это "секретный сигнал", который кнопка шлет бот
    builder.button(text="Купить", callback_data="buy_subscription")
    
    builder.adjust(1) 
    
    return builder.as_markup()



def get_period_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="📅 1 месяц", callback_data="buy_period_1m")],
        [InlineKeyboardButton(text="📅 3 месяца", callback_data="buy_period_3m")],
        [InlineKeyboardButton(text="📅 1 год", callback_data="buy_period_1y")],
        [InlineKeyboardButton(text="🔄 Назад", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)




def get_payment_keyboard(period_code: str) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="💳 Банковская карта (ЮMoney/T-Bank)", callback_data=f"pay_{period_code}_card")],
        [InlineKeyboardButton(text="💎 Криптовалюта (CryptoPay)", callback_data=f"pay_{period_code}_crypto")],
        [InlineKeyboardButton(text="⬅️ Назад к выбору периода", callback_data="buy_subscription")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)