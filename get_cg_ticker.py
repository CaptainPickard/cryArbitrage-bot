from pycoingecko import CoinGeckoAPI
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import config

cg = CoinGeckoAPI()
data = cg.get_coins_markets(vs_currency='usd')
list_1 = []

def get_cg_data():
    count = 0
    for i in data:
        if count <= 4:
            if 'usd' in i['symbol']:
                pass
            else:
                print(i['symbol'])
                list_1.append(i['symbol'])
                count += 1


get_cg_data()