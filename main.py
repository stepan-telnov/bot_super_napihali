from aiogram import executor
from config import dipip
from handlers import client, admin
 
client.register_handlers_client(dipip)  
admin.register_handlers_admin(dipip)


if __name__ == '__main__':
    executor.start_polling(dipip, skip_updates = True)