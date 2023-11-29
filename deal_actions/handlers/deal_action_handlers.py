from telebot import types

from buttons import back_button
from deal_actions import actions_with_deals
from deal_actions.actions_with_deals import check_open_deals, active_deal_sell_button_list
from keyboards.keyboards import start_panel_markup
from main import bot


@bot.message_handler(func=lambda message: message.text == "ACTIVE DEALS")
def handle_active_trades(message):
	response = check_open_deals()

	sell_button_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

	if response[0]:
		actions_with_deals.currency_to_sell_1_module = response[0]
		active_deal_sell_button_list.append(response[0])
		button = types.KeyboardButton(f'{response[0]}')
		sell_button_markup.add(button)

	if response[-1]:
		actions_with_deals.currency_to_sell_2_module = response[-1]
		active_deal_sell_button_list.append(response[-1])
		button = types.KeyboardButton(f'{response[-1]}')
		sell_button_markup.add(button)

	if not active_deal_sell_button_list:
		bot.send_message(message.chat.id, 'NO ACTIVE DEALS', reply_markup=start_panel_markup)
	else:
		sell_button_markup.add(back_button)
		bot.send_message(message.chat.id, 'ACTIVE DEALS:', reply_markup=sell_button_markup)


@bot.message_handler(func=lambda message: message.text == f"{actions_with_deals.currency_to_sell_1_module}")
def handle_sell_first(message):
	symbol = actions_with_deals.currency_to_sell_1_module
	response = f'CHOOSE ACTION FOR {symbol}'
	choose_action_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	sell_now_button = types.KeyboardButton(f'SELL {symbol} NOW')
	limit_button = types.KeyboardButton(f'LIMIT ORDER {symbol}')
	choose_action_markup.add(sell_now_button, limit_button, back_button)
	bot.send_message(message.chat.id, response, reply_markup=choose_action_markup)
