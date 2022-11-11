import ccxt
from get_cg_ticker import *

text = "_"

cmc_list = get_cg_data()

for cm in cmc_list:
    st = str(cm)
    ph = st.upper()
    try:
        binance = ccxt.binance() 
        bitfinex = ccxt.bitfinex() 
        bittrex = ccxt.bittrex() 
        poloniex = ccxt.poloniex() 
        bybit = ccxt.bybit()   
        gateio = ccxt.gate() 
        ftx = ccxt.ftx()    
        
        binance_ticker = binance.fetch_ticker(f'{ph}/USDT') 
        bitfinex_ticker = bitfinex.fetch_ticker(f'{ph}/USDT') 
        bittrex_ticker = bittrex.fetch_ticker(f'{ph}/USDT') 
        poloniex_ticker = poloniex.fetch_ticker(f'{ph}/USDT') 
        gateio_ticker = gateio.fetch_ticker(f'{ph}/USDT') 
        ftx_ticker = ftx.fetch_ticker(f'{ph}/USDT') 

    except Exception as e:
        # print(traceback.format_exc())
        # print(sys.exc_info()[2])
        print(f'\n{text:^10} *** <{ph}> Coin Not Found *** {text:^10}\n')


    binance_dif = float(binance_ticker['last'])
    bitfinex_dif = float(bitfinex_ticker['last'])
    bittrex_dif = float(bittrex_ticker['last'])
    poloniex_dif = float(poloniex_ticker['last'])
    gateio_dif = float(gateio_ticker['last'])
    ftx_dif = float(ftx_ticker['last'])

    path_list = {'Binance':binance_dif, 
                'Bitfinex':bitfinex_dif, 
                'Bittrex':bittrex_dif, 
                'Poloniex':poloniex_dif, 
                'Gateio':gateio_dif, 
                'FTX':ftx_dif}

    sort_path_dict = sorted(path_list.items(), key=lambda x:x[1])
    sorted_path_dict = dict(sort_path_dict)
    # print(sorted_path_dict)

    sorted_path_values = list(sorted_path_dict.values())
    sorted_path_keys = list(sorted_path_dict.keys())

    print(f'\n~{text:-^38}~\n')
    print(f'{ph:^40}')
    print(f'__-> Buy {ph} on {sorted_path_keys[0]}, Sell on {sorted_path_keys[-1]}')
    print(f' --> Arbitrage Dif: > {sorted_path_values[-1] - sorted_path_values[0]}')

    print(f"\n{text:_^40}\n")
# print(binance_ticker, bitfinex_ticker, bittrex_ticker, poloniex_ticker)

# Get top 5 coins by market cap   
            


















