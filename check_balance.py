from binance import Client
from config import API_KEY, API_SECRET


def check_balance():
	usdt_balance = 0

	try:
		client = Client(api_key=API_KEY, api_secret=API_SECRET)
		account_info = client.get_account()
		for balance in account_info['balances']:
			if balance['asset'] == 'USDT':
				usdt_balance = float(balance['free'])
		return f'BALANCE : {usdt_balance} USDT'
	except Exception as e:
		return f'BALANCE : {usdt_balance} USDT'
