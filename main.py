

import pandas as pd
import numpy as np
import yfinance as yf
from params import *
from utils import *


for market in MARKETS:
    
    #Get OHLCV data from yahoo finance
    data = yf.download(market, interval = CANDLE_PERIOD)
    
    
    #Calculate the RSI
    data['Change'] = data['Adj Close'].diff()
    data['Gain'] = data['Change'].mask(data['Change'] < 0, 0.0)
    data['Loss'] = -data['Change'].mask(data['Change'] > 0, -0.0)
    
    data['Avg Gain'] = rma(data['Gain'].to_numpy(), ROLLING_PERIOD)
    data['Avg Loss'] = rma(data['Loss'].to_numpy(), ROLLING_PERIOD)
    
    data['RS'] = data['Avg Gain'] / data['Avg Loss']
    data['RSI'] = 1 - (1 / (1 + data['RS']))
    
    
    #Calculate the MFI
    data['Typical Price'] = (data['Adj Close'] + data['High'] + data['Low']) / 3
    data['Money Flow'] = data['Typical Price'] * data['Volume']
    
    data['Positive Flow'], data['Negative Flow'] = np.nan, np.nan
    positive_flow = []
    negative_flow = []
    
    for i in range(1, len(data['Typical Price'])):
        if data['Typical Price'].iloc[i] > data['Typical Price'].iloc[i-1]:
            positive_flow.append(data['Money Flow'].iloc[i-1])
            negative_flow.append(0)
            
        elif data['Typical Price'].iloc[i] < data['Typical Price'].iloc[i-1]:
            negative_flow.append(data['Money Flow'].iloc[i-1])
            positive_flow.append(0)
            
        else:
            positive_flow.append(0)
            negative_flow.append(0)    
            
    data['Positive MF'] = data['Positive Flow'].rolling(ROLLING_PERIOD).sum()
    data['Negative MF'] = data['Negative Flow'].rolling(ROLLING_PERIOD).sum()    
            
    data['MFI'] = data['Positive MF']/ (data['Positive MF'] + data['Negative MF'])
    
    
    



