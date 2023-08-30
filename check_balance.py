from binance import Client
from telebot import types
from config import api_key, api_secret
check_button = types.KeyboardButton("CHECK BALANCE (USDT)")


def check_balance():
    usdt_balance = 0

    try:
        client = Client(api_key=api_key, api_secret=api_secret)
        account_info = client.get_account()
        for balance in account_info['balances']:
            if balance['asset'] == 'USDT':
                usdt_balance = float(balance['free'])
        return f'BALANCE : {usdt_balance} USDT'
    except Exception as e:
        return f'BALANCE : {usdt_balance} USDT'
