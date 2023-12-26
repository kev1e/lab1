from telebot import types
import telebot
import requests

bot = telebot.TeleBot('6922682877:AAEQpjTRGAUfJdJRrt4siZaFXGU7oiWFneM')

name = ''
surname = ''
age = 0


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, хочешь ввести свои данные? Напиши /reg.")
    elif message.text.lower() == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет или /reg.")
    elif message.text.lower() == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Сколько тебе лет?")
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    try:
        age = int(message.text)  # проверяем, что возраст введен корректно
    except Exception:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, get_age)
        return

    keyboard = types.InlineKeyboardMarkup()

    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')

    keyboard.add(key_yes)
    keyboard.add(key_no)

    question = f'Тебя зовут {name} {surname} и тебе {age} лет?'

    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Запомню : )')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Тогда напиши /reg еще раз.')


bot.polling(none_stop=True, interval=0)
