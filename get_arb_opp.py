import ccxt
import time

binance = ccxt.binance() 
bitfinex = ccxt.bitfinex() 
bittrex = ccxt.bittrex() 
poloniex = ccxt.poloniex() 


def get_input():
    global phrase, final
    phrase = input('Please enter a Crypto Acronym: >>> ')
    final = phrase.upper()

get_input()

binance_ticker = binance.fetch_ticker(f'{final}/USDT') 
bitfinex_ticker = bitfinex.fetch_ticker(f'{final}/USDT') 
bittrex_ticker = bittrex.fetch_ticker(f'{final}/USDT') 
poloniex_ticker = poloniex.fetch_ticker(f'{final}/USDT') 

# print(binance_ticker, bitfinex_ticker, bittrex_ticker, poloniex_ticker)


binance_dif = float(binance_ticker['last'])
print(f"Binance : {binance_dif}")

bitfinex_dif = float(bitfinex_ticker['last'])
print(f"Bitfinex : {bitfinex_dif}")

bittrex_dif = float(bittrex_ticker['last'])
print(f"Bittrex : {bittrex_dif}")

poloniex_dif = float(bittrex_ticker['last'])
print(f"Poloniex : {poloniex_dif}")



if binance_ticker['last'] < bitfinex_ticker['last']:
    print(f'> Buy {final} on Binance and sell on Bitfinex.') 
    print(f'Arbitrage Dif: > {bitfinex_dif - binance_dif}')
elif binance_ticker['last'] > bitfinex_ticker['last']: 
    print(f'> Buy {final} on Bitfinex and sell on Binance.') 
    print(f'Arbitrage Dif: > {binance_dif - bitfinex_dif}')
else:
    print('No arbitrage opportunity.') 



if binance_ticker['last'] < bittrex_ticker['last']: 
    print(f'> Buy {final} on Binance and sell on Bittrex.') 
    print(f'Arbitrage Dif: > {bittrex_dif - binance_dif}')
elif binance_ticker['last'] > bittrex_ticker['last']:
    print(f'> Buy {final} on Bittrex and sell on Binance.') 
    print(f'Arbitrage Dif: > {binance_dif- bittrex_dif}')
else:
    print('No arbitrage opportunity.') 



if binance_ticker['last'] < poloniex_ticker['last']: 
    print(f'> Buy {final} on Binance and sell on Poloniex.') 
    print(f'Arbitrage Dif: > {poloniex_dif - binance_dif}')
elif binance_ticker['last'] > poloniex_ticker['last']:
    print(f'> Buy {final} on Poloniex and sell on Binance.') 
    print(f'Arbitrage Dif: > {poloniex_dif - binance_dif}')
else:
    print('No arbitrage opportunity.') 