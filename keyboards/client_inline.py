from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton, WebAppInfo

def auth():
    inlineListClient = InlineKeyboardMarkup()

    btn1 = InlineKeyboardButton(text = "sign up", callback_data="signup")

    inlineListClient.add(btn1)
   

    return inlineListClient

def main_menu():
    inlineListClient = InlineKeyboardMarkup()

    btn2 = InlineKeyboardButton(text = "profile", callback_data="profile")
    btn3 = InlineKeyboardButton(text = "Pavel", web_app=WebAppInfo(url="https://github.com/pavelgodx"))
    btn4 = InlineKeyboardButton(text = "Stepanhkec", web_app=WebAppInfo(url="https://github.com/stepan-telnov"))

    inlineListClient.add(btn2)
    inlineListClient.add(btn4, btn3)

    return inlineListClient

def Back():
    inlineListClient = InlineKeyboardMarkup()

    btn1 = InlineKeyboardButton(text = "<-Back", callback_data="back_to_menu")

    inlineListClient.add(btn1)
    
    return inlineListClient