from aiogram import executor
from create_bot import dp

from HandlersBot import Start, SendVideoChat, Settings

# Register handlers
Start.register_handler_start(dp)
SendVideoChat.register_handler_send_video(dp)
Settings.register_handler_setting(dp)


executor.start_polling(dp, skip_updates=True)

