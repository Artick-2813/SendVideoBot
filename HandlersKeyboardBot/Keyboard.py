from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from DBase.Dbase import select_show_info_video


def menu_markup():
    btn_start = KeyboardButton('Отправить видео в чат 📩')
    btn_settings = KeyboardButton('Настройки ⚙')
    start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_start, btn_settings)

    return start_keyboard


def menu_settings():
    btn_show_info_video = KeyboardButton('Показывать информацию о видео 📝')
    btn_back = KeyboardButton('Назад 🔙')
    settings_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_show_info_video, btn_back)

    return settings_keyboard


def settings_show_info_video():
    status = select_show_info_video()
    if status == 'Выкл.':
        btn_enable = KeyboardButton('Вкл.')
        enable_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_enable)
        return enable_keyboard
    else:
        btn_disable = KeyboardButton('Выкл.')
        disable_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_disable)
        return disable_keyboard


def back_markup():
    btn_back = KeyboardButton('Назад 🔙')
    back_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_back)

    return back_keyboard
