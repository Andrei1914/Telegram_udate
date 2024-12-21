from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token='7992181640:AAGowdBVLBYenFGAgENw7nbqu6eP2c3_7jA')
dp = Dispatcher(bot, storage=MemoryStorage())