import telebot
from start_script import run_remote_script_first_module, start_button_first_module, start_button_second_module, \
    run_remote_script_second_module
from check_script import check_process_button, check_first_script, check_process_button2, check_second_script
from stop_script import stop_remote_script, stop_button
from check_balance import check_button, check_balance
from telebot import types
from config import allowed_users, API_TOKEN

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(func=lambda message: message.from_user.id not in allowed_users)
def ignore_other_users(message):
    user_id = message.from_user.id

    bot.send_message(user_id, 'У вас нет доступа к управлению ботом.')
    pass


@bot.message_handler(commands=['getchatid'])
def get_chat_id(message):
    chat_id = message.chat.id
    bot.reply_to(message, f'Ваш чат айди: {chat_id}')


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if user_id not in allowed_users:
        bot.send_message(user_id, 'У вас нет доступа к боту.')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(start_button_first_module, start_button_second_module, stop_button,
               check_process_button, check_process_button2, check_button,)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "CHECK MODULE 1")
def handle_check(message):
    response = check_first_script()
    bot.send_message(message.chat.id, response)


@bot.message_handler(func=lambda message: message.text == "CHECK MODULE 2")
def handle_check(message):
    response = check_second_script()
    bot.send_message(message.chat.id, response)


@bot.message_handler(func=lambda message: message.text == "START MODULE 1")
def handle_start_module1(message):
    response = run_remote_script_first_module()
    bot.send_message(message.chat.id, response)


@bot.message_handler(func=lambda message: message.text == "START MODULE 2")
def handle_start_module2(message):
    response = run_remote_script_second_module()
    bot.send_message(message.chat.id, response)


@bot.message_handler(func=lambda message: message.text == "CHECK BALANCE (USDT)")
def handle_check(message):
    response = check_balance()
    bot.send_message(message.chat.id, response)


@bot.message_handler(func=lambda message: message.text == "STOP BOT")
def handle_stop(message):
    response = stop_remote_script()
    bot.send_message(message.chat.id, response)


if __name__ == '__main__':
    try:
        bot.polling()
    except Exception as e:
        id = '5442883627'
        bot.send_message(id, f" ТЕЛЕГРАМ БОТ ОСТАНОВЛЕН. ВОЗНИКЛА ОШИБКА : {e}")
