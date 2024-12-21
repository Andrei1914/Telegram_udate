from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton('О нас', callback_data='О нас')], 
        [InlineKeyboardButton('Цены', callback_data='Купить')],
        [InlineKeyboardButton('Регистрация', callback_data='Регистрация')]
    ]
)

price_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton('Купить Напольные паралетсы', callback_data='Buy')], 
        [InlineKeyboardButton('Купить Настенный турник', callback_data='Buy')], 
        [InlineKeyboardButton('Купить Напольные брусья', callback_data='Buy')], 
        [InlineKeyboardButton('Купить Магнезию', callback_data='Buy')], 
        [InlineKeyboardButton('Другое', callback_data='Other')]
    ]
)

users_actions = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton('Список пользователей', callback_data='users')], 
        [InlineKeyboardButton('Статистика', callback_data='stat')], 
        [InlineKeyboardButton('Блокировка', callback_data='block')], 
        [InlineKeyboardButton('Разблокировка', callback_data='unblock')]
    ]
)