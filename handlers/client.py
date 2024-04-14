
from asyncio import sleep
import random

from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, InlineQuery,
                           InlineQueryResultArticle, InlineQueryResultPhoto,
                           InputTextMessageContent)
from aiogram.utils.callback_data import CallbackData

from config import bot, dipip
from db_handlers import Database
from keyboards.client_inline import *
from settings import ID_ADMINS_STEPASHKA_I_PAVEL
from States import StateRegistration


data_game = dict()  

db = Database("bot_super_napihali/data/data.db")


async def start_function(message:types.Message):
   await db.tabll()
   if await db.checkIdUser(message.from_user.id) == True:
      btn_menu = main_menu()
      await bot.send_message(message.from_user.id, "123", reply_markup = btn_menu)

   else:
      vauth = auth()
      await bot.send_message(message.from_user.id, "123", 
                             parse_mode=types.ParseMode.MARKDOWN_V2,
                             disable_web_page_preview = True, reply_markup = vauth)


async def get_info_user(call:types.CallbackQuery):
   await bot.delete_message(call.from_user.id,call.message.message_id)
   await bot.send_message(call.from_user.id, "😎💻enter your nickname🖥:")
   await StateRegistration.name.set()

async def validation_nickname(message:types.Message, state:FSMContext):
   async with state.proxy() as data:
      current_nickname = await db.ifNewUser(message.text)
      await bot.delete_message(message.from_user.id,message.message_id)
      await bot.delete_message(message.from_user.id,message.message_id -1)

      if current_nickname == True:
        await bot.send_message(message.from_user.id, "there is already such a user")
      else:
        data["name"] = message.text
        await bot.send_message(message.from_user.id, "enter your password")
        await StateRegistration.next()

async def validation_password(message:types.Message, state:FSMContext):
   async with state.proxy() as data:
      password = message.text
      data["password"] = password
      await bot.delete_message(message.from_user.id,message.message_id)
      await bot.delete_message(message.from_user.id,message.message_id -1)
      await db.createNewUser(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.username,
                             data["name"],
                             data["password"])
   await state.finish()
   btn_menu = main_menu()
   await bot.send_message(message.from_user.id, "123", reply_markup = btn_menu)

async def menushka(call:types.CallbackQuery, state:FSMContext):
   await state.finish()
   await bot.delete_message(call.from_user.id,call.message.message_id)
   btn_menu = main_menu()
   await bot.send_message(call.from_user.id, "123", reply_markup = btn_menu)

def register_handlers_client(dipip):
   dipip.register_message_handler(start_function, commands = ['start'])
   dipip.register_callback_query_handler(get_info_user, lambda x: x.data == "signup")
   dipip.register_callback_query_handler(menushka, lambda x: x.data == "back_to_menu", state = "*")
   dipip.register_message_handler(validation_nickname, state = StateRegistration.name)
   dipip.register_message_handler(validation_password, state = StateRegistration.password)