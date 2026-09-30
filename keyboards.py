from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_main_menu_keyboards() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    
    # Добавляем кнопки. callback_data — это "секретный сигнал", который кнопка шлет бот
    builder.button(text="Купить", callback_data="buy_subscription")
    
    # Показываем по 1 кнопке в ряду (можно поставить 2, чтобы были в одну строчку)
    builder.adjust(1) 
    
    return builder.as_markup()



def get_period_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="📅 1 неделя", callback_data="period_1_week")],
        [InlineKeyboardButton(text="📅 1 месяц", callback_data="period_1_month")],
        [InlineKeyboardButton(text="📅 3 месяца", callback_data="period_3_months")],
        [InlineKeyboardButton(text="📅 1 год", callback_data="period_1_year")],
        [InlineKeyboardButton(text="🔄 Назад", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)