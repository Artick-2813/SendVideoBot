from aiogram import types, Dispatcher
from DBase.Dbase import ChatIdDbase
from aiogram.dispatcher.filters import Text
from HandlersKeyboardBot.Keyboard import menu_markup, back_markup
from create_bot import bot, dp
from DBase.Dbase import select_show_info_video
from HandlersBot.SettingsVideo import conversion_duration_video, conversion_title_video


async def start_send_video(msg: types.Message):
    chat_id = msg.chat.id
    download_text = 'Пожалуйста, загрузите видео и я отправлю его в ваш чат ❗'

    await bot.send_message(chat_id, download_text, reply_markup=back_markup())
    
    @dp.message_handler(content_types=['video'])
    async def send_video(msg: types.Message):

        # Show or hidden info video
        show_info_video = select_show_info_video()

        chat_id = msg.chat.id
        # Info video
        id_video = msg.video.file_id
        file_name = msg.video.file_name
        duration_video = msg.video.duration
        title = conversion_title_video(file_name)
        duration = conversion_duration_video(duration_video)

        channel_id = ChatIdDbase(data=None).select_chat_id()

        try:
            if channel_id:
                if show_info_video == 'Выкл.':
                    await bot.send_video(channel_id, id_video)
                    await bot.send_message(chat_id, 'Видео успешно отправлено ✅', reply_markup=menu_markup())

                else:
                    message = f'{title}\n' \
                              f'Длительность видео: {duration}'
                    await bot.send_video(channel_id, id_video, caption=message)
                    await bot.send_message(chat_id, message)
                    await bot.send_message(chat_id, 'Видео успешно отправлено ✅', reply_markup=menu_markup())

        except Exception as ex:
            print(ex)
            error = 'Я не могу отправить видео в ваш чат,так как вы не ввели id вашего чата или был введен ' \
                    'неправльный id 😔.\n' \
                    'Пожалуйста, сохраните полученный id в настройках бота или измените неправильный id ❗'
            await bot.send_message(chat_id, error)


async def back_menu(msg: types.Message):
    chat_id = msg.chat.id

    await bot.send_message(chat_id, 'Возвращаюсь в меню ⬅', reply_markup=menu_markup())


def register_handler_send_video(dp: Dispatcher):
    dp.register_message_handler(start_send_video, lambda call: call.text == 'Отправить видео в чат 📩')
    dp.register_message_handler(back_menu, Text(equals='Назад 🔙'))
