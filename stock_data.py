import urllib.request
from alpha_vantage.timeseries import TimeSeries
from datetime import date, datetime, timedelta
import os

apiKey = os.getenv('STOCK_KEY')
stock_sym = ['GOOGL','FB']
ts = TimeSeries(apiKey)


def weekday():
    today_date = date.today()
    weekday = today_date.weekday()

    if weekday <= 4:
        return today_date
    elif weekday == 5 : 
        return datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    else: 
        return datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')


def vatage_stock_data(date):
    vantage_data = []
    local_stock_list = []

    for symbol in stock_sym:
        symbol, meta = ts.get_daily(symbol=f'{symbol}')
        vantage_data.append(symbol[f'{date}'])

    for line,name in zip(vantage_data,stock_sym):
        new_dict={f'{name}':line}
        local_stock_list.append(new_dict)

    return local_stock_list

def stock_open(list):
    for i in range(len(list)):
        for symbol,value in list[i].items():
            print("OPEN",symbol,value['1. open'],sep="-")
    print("\n")

def stock_high(list):
    for i in range(len(list)):
        for symbol,value in list[i].items():
            print("HIGH",symbol,value['2. high'],sep="-")
    print("\n")

def stock_low(list):
    for i in range(len(list)):
        for symbol,value in list[i].items():
            print("LOW",symbol,value['3. low'],sep=":")
    print("\n")

def stock_close(list):
    for i in range(len(list)):
        for symbol,value in list[i].items():
            print("ClOSE",symbol,value['4. close'],sep="-")
    print("\n")

weekday = weekday()
stock_data = vatage_stock_data(weekday)

stock_open(stock_data)
stock_high(stock_data)
stock_low(stock_data)
stock_close(stock_data)
