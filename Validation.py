from aiogram import executor
from config import dipip
from handlers import client
from settings import ID_ADMINS_STEPASHKA_I_PAVEL

def ifAdmin (tg_id):
    if tg_id in ID_ADMINS_STEPASHKA_I_PAVEL:
        return True
    else:
        return False
print (ifAdmin("5566865283"))