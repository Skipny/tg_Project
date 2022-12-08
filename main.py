import telebot
from telebot import types
from time import sleep
from TOKEN import token, chat_id
# передаем токен
bot = telebot.TeleBot(token)
#команда для старта бота
@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = types.KeyboardButton(text = "Добавить уведомление")#Объявление конопки
    markup.add(keyboard)#Добавление кнопки
    bot.send_message(chat_id, "Привет", reply_markup=markup)#реакция на команду start
#Метод реагирует на нажатие кнопки "Добавить уведомление"
@bot.message_handler(content_types=["text"])
def text_msg(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if message.text == "Добавить уведомление":
            pog = bot.send_message(chat_id, 'Добавьте текст уведомления')
            # ожидание пока пользователь введет текст уведомления
            # и отправляет введеный текст в метод InlineBtnBlock
            bot.register_next_step_handler(pog, InlineBtnBlock)


def InlineBtnBlock(message):
    global notification_msg
    # т.к. принимаймый текст содержит лишние символы форматируем сообщение
    notification_msg = ' {pog}'.format(pog=message.text)
    # добавляем кнопки в нутри сообщения
    inline_markup = types.InlineKeyboardMarkup(row_width=True)
    inline_keyboard = types.InlineKeyboardButton("1 мин", callback_data=1)
    inline_keyboard2 = types.InlineKeyboardButton("5 мин", callback_data=2)
    inline_keyboard3 = types.InlineKeyboardButton("10 мин", callback_data=3)
    inline_keyboard4 = types.InlineKeyboardButton("15 мин", callback_data=4)
    inline_keyboard5 = types.InlineKeyboardButton("30 мин", callback_data=5)
    inline_keyboard6 = types.InlineKeyboardButton("60 мин", callback_data=6)
    # Добавление кнопок
    inline_markup.add(inline_keyboard, inline_keyboard2, inline_keyboard3, inline_keyboard4,
                      inline_keyboard5,inline_keyboard6)
    #сообщение предлагает пользователю выбрать через сколько придет уведомление
    #и отправлеят кнопки с указанным временем
    bot.send_message(chat_id, "Выбирите через сколько придет уведомление", reply_markup=inline_markup)


#Метод обратной связи на нажатую кнопку из метода InlineBtnBlock
@bot.callback_query_handler(func=lambda call:True)
def callback_data(call):
    photo = open('artworks-000117207010-ao4lrg-t500x500.jpg', 'rb')
    if call.message:
        if call.data == '1':
            #slep считает в секундах
            sleep(1*60)
            # отправляет фото и текст введенный пользователем через заданное время
            bot.send_photo(call.message.chat.id, photo, caption=notification_msg)
        elif call.data == '2':
            sleep(5 * 60)
            bot.send_photo(call.message.chat.id, photo, caption=notification_msg)
        elif call.data == '3':
            sleep(10 * 60)
            bot.send_photo(call.message.chat.id, photo, caption=notification_msg)
        elif call.data == '4':
            sleep(15 * 60)
            bot.send_photo(call.message.chat.id, photo, caption=notification_msg)
        elif call.data == '5':
            sleep(30 * 60)
            bot.send_photo(call.message.chat.id, photo, caption=notification_msg)
        elif call.data == '6':
            sleep(60 * 60)
            bot.send_photo(call.message.chat.id, photo, caption=notification_msg)

bot.polling(none_stop=True)
