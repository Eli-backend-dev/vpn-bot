from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_main_inline_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    
    # Добавляем кнопки. callback_data — это "секретный сигнал", который кнопка шлет боту
    builder.button(text="👤 Мой профиль", callback_data="profile")
    builder.button(text="ℹ️ О боте", callback_data="about")
    
    # Показываем по 1 кнопке в ряду (можно поставить 2, чтобы были в одну строчку)
    builder.adjust(1) 
    
    return builder.as_markup()