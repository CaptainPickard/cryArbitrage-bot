import ccxt
import time

binance = ccxt.binance() 
bitfinex = ccxt.bitfinex() 
bittrex = ccxt.bittrex() 
poloniex = ccxt.poloniex() 
bybit = ccxt.bybit()   
gateio = ccxt.gate() 
ftx = ccxt.ftx() 
text = "_"


prog = True
while prog is True:

    phrase = input('Please enter a Crypto Acronym: >>> ')
    final = phrase.upper()
    

    binance_ticker = binance.fetch_ticker(f'{final}/USDT') 
    bitfinex_ticker = bitfinex.fetch_ticker(f'{final}/USDT') 
    bittrex_ticker = bittrex.fetch_ticker(f'{final}/USDT') 
    poloniex_ticker = poloniex.fetch_ticker(f'{final}/USDT') 
    gateio_ticker = gateio.fetch_ticker(f'{final}/USDT') 
    ftx_ticker = ftx.fetch_ticker(f'{final}/USDT') 

    # print(binance_ticker, bitfinex_ticker, bittrex_ticker, poloniex_ticker)
    
    print(f"\n{text:_^30}\n")

    binance_dif = float(binance_ticker['last'])
    print(f"--> Binance : {binance_dif:^5}")

    bitfinex_dif = float(bitfinex_ticker['last'])
    print(f"--> Bitfinex : {bitfinex_dif:^5}")

    bittrex_dif = float(bittrex_ticker['last'])
    print(f"--> Bittrex : {bittrex_dif:^5}")

    poloniex_dif = float(poloniex_ticker['last'])
    print(f"--> Poloniex : {poloniex_dif:^5}")

    gateio_dif = float(gateio_ticker['last'])
    print(f"--> Gateio : {gateio_dif:^5}")

    ftx_dif = float(ftx_ticker['last'])
    print(f"--> FTX : {ftx_dif:^5}")

    print(f"\n{text:_^30}\n")



    def find_optimal_path():
        path_list = {'Binance':binance_dif, 
                     'Bitfinex':bitfinex_dif, 
                     'Bittrex':bittrex_dif, 
                     'Poloniex':poloniex_dif, 
                     'Gateio':gateio_dif, 
                     'FTX':ftx_dif}

        sorted_path_dict = sorted(path_list.items(), key=lambda x:x[1])
        # print(sorted_path_dict)

        # sorted_path_list = list(sorted_path_dict.values())

        print('~Optimal Exchange Trade Path~')
        print(f'Buy on {str(sorted_path_dict[0])}, Sell on {str(sorted_path_dict[-1])}')
        # print(f'Arbitrage Dif: > {sorted_path_dict[0] - sorted_path_dict[-1]}')

        print(f"\n{text:_^30}\n")

    find_optimal_path()    


    # Binance & Bitfinex
    if binance_ticker['last'] < bitfinex_ticker['last']:
        print(f'> Buy {final} on Binance and sell on Bitfinex.') 
        print(f'Arbitrage Dif: > {bitfinex_dif - binance_dif}')
    elif binance_ticker['last'] > bitfinex_ticker['last']: 
        print(f'> Buy {final} on Bitfinex and sell on Binance.') 
        print(f'Arbitrage Dif: > {binance_dif - bitfinex_dif}')
    else:
        print('No arbitrage opportunity.') 
    print(f"\n{text:_^10}\n")


    # Bianace & Bittrex
    if binance_ticker['last'] < bittrex_ticker['last']: 
        print(f'> Buy {final} on Binance and sell on Bittrex.') 
        print(f'Arbitrage Dif: > {bittrex_dif - binance_dif}')
    elif binance_ticker['last'] > bittrex_ticker['last']:
        print(f'> Buy {final} on Bittrex and sell on Binance.') 
        print(f'Arbitrage Dif: > {binance_dif- bittrex_dif}')
    else:
        print('No arbitrage opportunity.') 
    print(f"\n{text:_^10}\n")


    # Bianace & Poloniex
    if binance_ticker['last'] < poloniex_ticker['last']: 
        print(f'> Buy {final} on Binance and sell on Poloniex.') 
        print(f'Arbitrage Dif: > {poloniex_dif - binance_dif}')
    elif binance_ticker['last'] > poloniex_ticker['last']:
        print(f'> Buy {final} on Poloniex and sell on Binance.') 
        print(f'Arbitrage Dif: > {binance_dif - poloniex_dif}')
    else:
        print('No arbitrage opportunity.') 
    print(f"\n{text:_^10}\n")


    # Bianace & Gateio
    if binance_ticker['last'] < gateio_ticker['last']: 
        print(f'> Buy {final} on Binance and sell on Gateio.') 
        print(f'Arbitrage Dif: > {gateio_dif - binance_dif}')
    elif binance_ticker['last'] > gateio_ticker['last']:
        print(f'> Buy {final} on Gateio and sell on Binance.') 
        print(f'Arbitrage Dif: > {binance_dif - gateio_dif}')
    else:
        print('No arbitrage opportunity.') 
    print(f"\n{text:_^10}\n")


    # Bianace & FTX
    if binance_ticker['last'] < ftx_ticker['last']: 
        print(f'> Buy {final} on Binance and sell on FTX.') 
        print(f'Arbitrage Dif: > {ftx_dif - binance_dif}')
    elif binance_ticker['last'] > ftx_ticker['last']:
        print(f'> Buy {final} on FTX and sell on Binance.') 
        print(f'Arbitrage Dif: > {binance_dif - ftx_dif}')
    else:
        print('No arbitrage opportunity.') 
    print(f"\n{text:_^10}\n")


    exit_input = input("Would you like to exit? y/n >>> ")
    if exit_input == 'y':
        prog = False
        break