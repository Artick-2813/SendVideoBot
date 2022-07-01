from aiogram import types, Dispatcher
from create_bot import bot
from HandlersKeyboardBot.Keyboard import menu_markup
from DBase.Dbase import create_database


async def start(msg: types.Message):
    chat_id = msg.chat.id
    full_name_user = msg.from_user.full_name

    # Create Database
    create_database()

    await bot.send_message(chat_id, f'Приветствую тебя ✋, {full_name_user}!\n'
                                    f'Хочешь отправить видео 🤔, тогда нажми на кнопку 👇', reply_markup=menu_markup())


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
