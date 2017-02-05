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
returns = price.pct_change()

# 1. Find the trend
