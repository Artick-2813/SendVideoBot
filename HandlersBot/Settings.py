from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import bot
from HandlersKeyboardBot.Keyboard import menu_settings, settings_show_info_video, menu_markup, back_markup
from DBase.Dbase import *


class Settings(StatesGroup):
    show_information_video = State()
    your_chat_id = State()


async def settings(msg: types.Message):
    chat_id = msg.chat.id

    await bot.send_message(chat_id, 'Что хотите изменить?', reply_markup=menu_settings())


async def show_info_video(msg: types.Message):

    chat_id = msg.chat.id
    await bot.send_message(chat_id, 'Выберите, что вам нужно изменить', reply_markup=settings_show_info_video())

    await Settings.show_information_video.set()


async def save_change(msg: types.Message, state: FSMContext):
    change = msg.text
    chat_id = msg.chat.id

    await state.update_data(show_info_video=change)

    await bot.send_message(chat_id, change, reply_markup=menu_markup())

    data = await state.get_data()
    status = data['show_info_video']

    # Update settings when user choose what does he need
    update_show_info_video(status)
    await bot.send_message(chat_id, 'Изменения сохранены ✅', reply_markup=menu_markup())
    await state.reset_state(with_data=False)


async def your_chat_id(msg: types.Message):
    chat_id = msg.chat.id

    await bot.send_message(chat_id, 'Напишите свой полученный id чата', reply_markup=types.ReplyKeyboardRemove())

    await Settings.your_chat_id.set()


async def save_chat_id(msg: types.Message, state: FSMContext):
    id_telegram_chat = msg.text
    chat_id = msg.chat.id

    await state.update_data(your_chat_id=id_telegram_chat)

    await bot.send_message(chat_id, id_telegram_chat)

    data = await state.get_data()
    status = data['your_chat_id']

    # Save chat id telegram in DataBase
    ChatIdDbase(status).update_chat_id()
    await bot.send_message(chat_id, 'Изменения сохранены ✅', reply_markup=menu_markup())
    await state.reset_state(with_data=False)


async def back_menu(msg: types.Message):
    chat_id = msg.chat.id

    await bot.send_message(chat_id, 'Возвращаюсь в меню ⬅', reply_markup=menu_markup())


def register_handler_setting(dp: Dispatcher):
    dp.register_message_handler(settings, lambda call: call.text == 'Настройки ⚙')
    dp.register_message_handler(show_info_video, lambda call: call.text == 'Показывать информацию о видео 📝')
    dp.register_message_handler(your_chat_id, lambda call: call.text == 'Сохранение chat id ☑')

    dp.register_message_handler(save_change, state=Settings.show_information_video)
    dp.register_message_handler(save_chat_id, state=Settings.your_chat_id)
    dp.register_message_handler(back_menu, Text(equals='Назад 🔙'))



