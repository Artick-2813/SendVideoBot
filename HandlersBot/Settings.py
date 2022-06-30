from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import bot
from HandlersKeyboardBot.Keyboard import menu_settings, settings_show_info_video, menu_markup
from DBase.Dbase import update_show_info_video


class Settings(StatesGroup):
    show_information_video = State()


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
    await bot.send_message(chat_id, 'Изменения сохранены ✅')
    await state.reset_state(with_data=False)


async def back_menu(msg: types.Message):
    chat_id = msg.chat.id

    await bot.send_message(chat_id, 'Возвращаюсь в меню ⬅', reply_markup=menu_markup())


def register_handler_setting(dp: Dispatcher):
    dp.register_message_handler(settings, lambda call: call.text == 'Настройки ⚙')
    dp.register_message_handler(show_info_video, lambda call: call.text == 'Показывать информацию о видео 📝')

    dp.register_message_handler(save_change, state=Settings.show_information_video)
    dp.register_message_handler(back_menu, Text(equals='Назад 🔙'))



