from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def getInfoUsers():
    buttonList = InlineKeyboardMarkup()
    btn2 = InlineKeyboardButton("Database user table📄",callback_data="Database_user_table")
    btn3 = InlineKeyboardButton("User annihilation 🗿〰🔫",callback_data="User_annihilation")
    buttonList.add(btn2)
    buttonList.add(btn3)
    return buttonList
    