import csv

import telebot

from keyboards.keyboards import start_panel_markup, data_base_markup, limit_markup
from buttons import back_button
from start_script import run_remote_script
from check_script import check_bot_script
from stop_script import stop_remote_script
from check_balance import check_balance
from telebot import types
from config import ALLOWED_USERS, API_TOKEN, DATA_BASE_PATCH, COMMANDS_PATCH
from flask import Flask, request
from deal_actions.actions_with_deals import check_open_deals, active_deal_sell_button_list
import traceback
from deal_actions import actions_with_deals

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)


@bot.message_handler(func=lambda message: message.from_user.id not in ALLOWED_USERS)
def ignore_other_users(message):
	user_id = message.from_user.id

	bot.send_message(user_id, 'У вас нет доступа к управлению ботом.')
	pass


@bot.message_handler(commands=['get_chat_id'])
def get_chat_id(message):
	chat_id = message.chat.id
	bot.reply_to(message, f'Ваш чат айди: {chat_id}')


@bot.message_handler(commands=['start'])
def start(message):
	user_id = message.from_user.id
	if user_id not in ALLOWED_USERS:
		bot.send_message(user_id, 'У вас нет доступа к боту.')

	bot.send_message(message.chat.id, "ACTION:", reply_markup=start_panel_markup)


@bot.message_handler(func=lambda message: message.text == "CHECK BOT")
def handle_check(message):
	response = check_bot_script()
	bot.send_message(message.chat.id, response)


@bot.message_handler(func=lambda message: message.text == "DATABASE")
def handle_base(message):
	bot.send_message(message.chat.id, "CHOOSE ACTION:", reply_markup=data_base_markup)


@bot.message_handler(func=lambda message: message.text == "CLEAR DATABASE")
def clear_database_handle(message):
	bot.send_message(message.chat_id, 'RESERVE DATABASE COPY')
	handle_download_base(message)
	try:
		with open(DATA_BASE_PATCH, 'r', newline='') as file:
			reader = csv.reader(file)
			header = next(reader, None)

		with open(DATA_BASE_PATCH, 'w', newline='') as file:
			writer = csv.writer(file)
			if header:
				writer.writerow(header)

		bot.send_message(message.chat.id, 'DATABASE CLEARED', reply_markup=data_base_markup)
	except Exception as exp:
		bot.send_message(message.chat.id, str(exp))


@bot.message_handler(func=lambda message: message.text == "DOWNLOAD DATABASE")
def handle_download_base(message):
	with open(DATA_BASE_PATCH, 'rb') as csv_document:
		bot.send_document(message.chat.id, csv_document)


@bot.message_handler(func=lambda message: message.text == "START BOT")
def handle_start_module1(message):
	response = run_remote_script()
	bot.send_message(message.chat.id, response)


@bot.message_handler(func=lambda message: message.text == "CHECK BALANCE (USDT)")
def handle_check(message):
	response = check_balance()
	bot.send_message(message.chat.id, response)


@bot.message_handler(func=lambda message: message.text == "STOP BOT")
def handle_stop(message):
	response = stop_remote_script()
	bot.send_message(message.chat.id, response)


@bot.message_handler(func=lambda message: message.text == "BACK")
def handle_back(message):
	bot.send_message(message.chat.id, "ACTION:", reply_markup=start_panel_markup)


# ACTIONS THAT NEED A VARIABLE(CURRENCY NAME)
'''FIRST DEAL'''


@bot.message_handler(func=lambda message: message.text == f"SELL {actions_with_deals.currency_to_sell_1_module} NOW")
def handle_sell_first(message):
	symbol = actions_with_deals.currency_to_sell_1_module
	response = f'SELL {symbol} NOW'
	with open(f'{COMMANDS_PATCH}1_{symbol}', 'w') as f:
		pass
	actions_with_deals.currency_to_sell_1_module = None
	if actions_with_deals.currency_to_sell_2_module:
		button = types.KeyboardButton(f'{actions_with_deals.currency_to_sell_2_module}')
		sell_button_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		sell_button_markup.add(button, back_button)
		bot.send_message(message.chat.id, response, reply_markup=sell_button_markup)
	else:
		bot.send_message(message.chat.id, response, reply_markup=start_panel_markup)


@bot.message_handler(func=lambda message: message.text == f"LIMIT ORDER {actions_with_deals.currency_to_sell_1_module}")
def handle_sell_first(message):
	symbol = actions_with_deals.currency_to_sell_1_module
	response = f'CHOOSE ACTION FOR {symbol}:'
	bot.send_message(message.chat.id, response, reply_markup=limit_markup)


'''END OF FIRST DEAL'''

'''SECOND DEAL'''


@bot.message_handler(func=lambda message: message.text == f'{actions_with_deals.currency_to_sell_2_module}')
def handle_sell_second(message):
	symbol = actions_with_deals.currency_to_sell_2_module
	response = f'CHOOSE ACTION FOR {symbol}'
	choose_action_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	sell_now_button = types.KeyboardButton(f'SELL {symbol} NOW')
	limit_button = types.KeyboardButton(f'LIMIT ORDER {symbol}')
	choose_action_markup.add(sell_now_button, limit_button, back_button)
	bot.send_message(message.chat.id, response, reply_markup=choose_action_markup)


@bot.message_handler(func=lambda message: message.text == f"SELL {actions_with_deals.currency_to_sell_2_module} NOW")
def handle_sell_first(message):
	symbol = actions_with_deals.currency_to_sell_2_module
	response = f'SELL {symbol} NOW'
	with open(f'{COMMANDS_PATCH}1_{symbol}', 'w') as f:
		pass
	actions_with_deals.currency_to_sell_2_module = None
	if actions_with_deals.currency_to_sell_1_module:
		button = types.KeyboardButton(f'SELL {actions_with_deals.currency_to_sell_1_module}')
		sell_button_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		sell_button_markup.add(button, back_button)
		bot.send_message(message.chat.id, response, reply_markup=sell_button_markup)
	else:
		bot.send_message(message.chat.id, response, reply_markup=start_panel_markup)


@bot.message_handler(func=lambda message: message.text == f"LIMIT ORDER {actions_with_deals.currency_to_sell_2_module}")
def handle_sell_first(message):
	symbol = actions_with_deals.currency_to_sell_2_module
	response = f'CHOOSE ACTION FOR {symbol}:'
	bot.send_message(message.chat.id, response, reply_markup=limit_markup)


'''END OF SECOND DEAL'''


def limit_order_handler(message, symbol):
	price = message.text

	with open(f'{COMMANDS_PATCH}2_{symbol}_{price}', 'w') as f:
		pass
	response = f'limit for {symbol} was set successfully'.upper()
	actions_with_deals.currency_to_sell_1_module = None
	if actions_with_deals.currency_to_sell_2_module:
		button = types.KeyboardButton(f'{actions_with_deals.currency_to_sell_2_module}')
		sell_button_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		sell_button_markup.add(button, back_button)
		bot.send_message(message.chat.id, response, reply_markup=sell_button_markup)
	else:
		bot.send_message(message.chat.id, response, reply_markup=start_panel_markup)


# bot.register_next_step_handler(message, limit_order_handler, symbol)


# END OF ACTION THAT NEEDS CURRENCY NAME
@app.route('/webhook', methods=['POST'])
def webhook():
	update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
	bot.process_new_updates([update])
	return "OK"


if __name__ == '__main__':
	try:

		bot.remove_webhook()
		bot.set_webhook(url="https://vm4624807.34ssd.had.wf/webhook")
		app.run(host='127.0.0.1', port=5000)
	except Exception as e:
		traceback_str = traceback.format_exc()
		id = '5442883627'
		bot.send_message(id, f"EXCEPTION IN TELEGRAM BOT :{traceback_str}")
