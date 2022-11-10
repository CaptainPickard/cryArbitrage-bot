from pycoingecko import CoinGeckoAPI
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import config

cg = CoinGeckoAPI()
data = cg.get_coins_markets(vs_currency='usd')
list_1 = []
count = 0

def get_cg_data():
    for i in data:
        if count <= 5:
            if i['symbol'] == 'usdt':
                pass
            else:
                print(i['symbol'])
                list_1.append(i['symbol'])


get_cg_data()