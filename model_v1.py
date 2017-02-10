"""
Plain coding model: 
Input: one-dimensional data 
Output: Profit for one-year investment 
Coding method: plain script coding, line by line, like code in R 
Mission: Explore the performance of strategy in perfect scenario (no cost, instant trading, etc.)
"""
import numpy as np
from matplotlib import pylab, mlab, pyplot
plt = pyplot
import pandas as pd
from pandas import DataFrame, Series
#import pandas.io.data as web
from pandas_datareader import data as web

# 0. download and prepare the data
data = {}
for ticker in ['GOOG']:
    data[ticker] = web.get_data_yahoo(ticker, '1/1/2008','1/1/2017')

price = DataFrame({tic:data['Adj Close'] for tic,data in data.iteritems()})
volume = DataFrame({tic:data['Volume'] for tic,data in data.iteritems()})

# 1. Find the trend

# 1.1 Calculate moving average
tick = 'GOOG'
span = 15

def movingAverage(data,span = 15):
    """
    return a scalar price as the moving averager of given data
    """
    if len(data) != span:
        raise ValueError("Check the size of input data")
    
    return data.sum()/span


average = [] 
for i in range(span-1,len(price)):
    average.append(movingAverage(price[tick].iloc[i-(span-1):i+1],span))
res = Series(average, index = price.index[span-1:],name = 'moav').shift(1)
data = price.join(res).dropna()

# 1.2 Get momentum counts by comparing price today with average yesterday

def getMomentumNum(data):
    """ assign a number to indicate momentum status
        return an array of int number
    """
    count = 0
    result = []
    index = data.index
    for ind,row in data.iterrows():
        d = row[tick]-row['moav']
        if (d*count) >= 0:
            if d >= 0: 
                count+=1
            else:
                count -= 1
        else:
            if d >= 0:
                count = 1
            else:
                count = -1
        result.append(count)
    return Series(result,index = index, name = 'MomNum')


num = getMomentumNum(data)
data = data.join(num)


# 2. Buy and sell the stock at specified time

def getTradingData(data, buy_value = 5, sell_value = -3):
    hasStock = False
    res = []
    status = []
    for ind,row in data.iterrows():
        if not hasStock and row['MomNum'] == buy_value:
            hasStock = True
            res.append((ind,row[tick]))
            status.append('Buy')
        if hasStock and row['MomNum'] == sell_value:
            hasStock = False
            res.append((ind,row[tick]))
            status.append('Sell')
    return pd.Series(dict(res)),status

trade,status = getTradingData(data)
            
res = trade.groupby(status).prod()
profit = res['Sell']/res['Buy']-1

print "The profit from {} to {} is {:2%}".format(price.index[0].strftime("%Y-%m-%d"),
                                        price.index[-1].strftime("%Y-%m-%d"),profit)

