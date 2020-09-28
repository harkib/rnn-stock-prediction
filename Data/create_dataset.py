import yfinance as yf
import pandas as pd 
import pickle
from datetime import datetime

if __name__ == '__main__':

    companies = pd.read_csv('NASDEQ_compaines.csv')
    symbols = companies['Symbol']

    start = datetime(2018,10,1,0,0,0)
    end = datetime(2020,9,27,0,0,0)
    interval = '1h'

    # multiple symbols at 1h interval fials, need loop
    results = pd.DataFrame()
    for symbol in symbols:
        result = yf.download(symbol, start= start, end= end ,interval = interval,prepost = True,threads = False)

        # when doing any interval greater than a day there are 
        # NAN values returned for days with dividend payout
        result = result.dropna(axis=0, how='any') 

        result = result.groupby('Date').agg(lambda x: list(x))
        result['Symbol'] = symbol

        results = results.append(result, ignore_index = True)

    # save
    results.to_pickle('NASDEQ_data.pkl')


