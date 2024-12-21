from aiogram import executor
from config import *
import texts
from keyboards import *
from admin import *
from crud_functions import *
from aiogram.dispatcher.filters.state import State, StatesGroup

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000

initiate_db()

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer(f"{message.from_user.username}, добро пожаловать в наш магазин! "+texts.starts, reply_markup = start_kb)

@dp.callback_query_handler(text="Регистрация")
async def sing_up(call):
    await call.message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()    

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_include(message.text):
        await message.answer("Пользователь существует, введите другое имя: ")
        await RegistrationState.username.set()
    else:
        await state.update_data(username = message.text) 
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email = message.text)    
    await message.answer("Введите ваш возраст:")
    await RegistrationState.age.set()   

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age = message.text)   
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer("Регистрация пройдена!")   

@dp.callback_query_handler(text = "О нас")
async def price_message(call):
    await call.message.answer(texts.about, reply_markup = start_kb)
    await call.answer()

@dp.callback_query_handler(text ="Купить")
async def about_message(call):
    for product in get_all_products():
        await call.message.answer(f"{product[1]}\n{product[2]}\nЦена: {product[3]} руб")
        with open(f'image\{product[1]}.jpg', 'rb') as img:
            await call.message.answer_photo(img)

    await call.message.answer("Купить: ", reply_markup = price_kb)

@dp.callback_query_handler(text = "Buy")
async def other_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

@dp.callback_query_handler(text = "Other")
async def other_message(call):
    await call.message.answer(texts.other_work)
    await call.answer()

if __name__ =='__main__':
    executor.start_polling(dp, skip_updates=True)

