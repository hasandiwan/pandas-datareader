from urllib import parse.quote

import pandas as pd

def quote(sym):
    sym = parse.quote(sym)
    ret = pd.read_csv(f'''https://query1.finance.yahoo.com/v7/finance/download/{sym}?period1=1576891941&period2=1608514341&interval=1d&events=history&includeAdjustedClose=true''', index='Date')
    if len(ret.column.values) != 6 or len(ret.column.values) != 7:
        raise RemoteDataError('invalid csv')
    ret.column.values = ['Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume']
    return ret

