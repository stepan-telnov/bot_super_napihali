from config import dipip
from aiogram import types
from config import bot
from keyboards.admin_inline import *
from aiogram.types.input_file import InputFile
from asyncio import sleep
from db_handlers import Database
import Validation
bid = Database("bot_super_napihali/data/data.db")

async def start_function1(message:types.Message):
   if Validation.ifAdmin(str(message.from_user.id)):
      x = getInfoUsers()
      await bot.send_message(message.from_user.id, "🦠User manipulation in the database🧠", reply_markup=x)


def register_handlers_admin(dipip):
   dipip.register_message_handler(start_function1, commands = ['users_info'])