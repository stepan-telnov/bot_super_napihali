from aiogram import Bot, Dispatcher 
import settings
from aiogram.contrib.fsm_storage.memory import MemoryStorage
bot = Bot(token = settings.TOKEN)

memory = MemoryStorage()

#db is my database name
dipip = Dispatcher(bot, storage = memory)