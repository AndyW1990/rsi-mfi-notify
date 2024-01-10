

import pandas as pd
import numpy as np
import yfinance as yf
import ssl
from smtplib import SMTP
from params import *

def run_markets(test=False, test_rsi=0.6, test_mfi=0.6):

    #main loop over markets in params
    for market in MARKETS:
        
        #Get OHLCV data from yahoo finance
        data = yf.download(market, interval = CANDLE_PERIOD)
        
        
        #Calculate the RSI
        data['Change'] = data['Adj Close'].diff()
        data['Gain'] = data['Change'].mask(data['Change'] < 0, 0.0)
        data['Loss'] = -data['Change'].mask(data['Change'] > 0, -0.0)
        
        data['Avg Gain'] = data['Gain'].rolling(ROLLING_PERIOD).mean()
        data['Avg Loss'] = data['Loss'].rolling(ROLLING_PERIOD).mean()
        
        data['RS'] = data['Avg Gain'] / data['Avg Loss']
        data['RSI'] = 1 - (1 / (1 + data['RS']))
        
        
        #Calculate the MFI
        data['Typical Price'] = (data['Adj Close'] + data['High'] + data['Low']) / 3
        data['Money Flow'] = data['Typical Price'] * data['Volume']
               
        positive_flow = [np.nan]
        negative_flow = [np.nan]
        
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
                
        data['Positive Flow'] = positive_flow
        data['Negative Flow'] = negative_flow
                
        data['Positive MF'] = data['Positive Flow'].rolling(ROLLING_PERIOD).sum()
        data['Negative MF'] = data['Negative Flow'].rolling(ROLLING_PERIOD).sum()    
                
        data['MFI'] = data['Positive MF']/ (data['Positive MF'] + data['Negative MF'])
        
        if test:
            rsi = test_rsi
            mfi = test_mfi
        else:
            #take end of last week info (don't take current partial week)
            rsi = data['RSI'].iloc[-2]
            mfi = data['MFI'].iloc[-2]
        
        
        #Create message if oversold/overbought
        if rsi >= 0.7 and mfi >= 0.7:
            message = f'{market} is overbought, sell a percentage of stock! \nRSI = {rsi:.2f} \nMFI = {mfi:.2f}'
            send = True
        elif rsi <= 0.5 and mfi <= 0.5:
            message = f'{market} is oversold, consider buying some stock. \nRSI = {rsi:.2f} \nMFI = {mfi:.2f}'
            send = True
        else:
            message = f'{market} is neither oversold nor overbought. \nRSI = {rsi:.2f} \nMFI = {mfi:.2f}'
            send = False
        
        #send email if required
        if send:
            print_message = f'Sending email as {message}'
            
            #contruct email, must be formatted without whitespace as AWS is fussy  
            email = f"""From: {SES_FROM}
To: {SES_TO}
Subject: Notice of significant change in {market}\n
{message}"""

            # setting up ssl context
            context = ssl.create_default_context()
            
            with SMTP(SES_HOST_ADDRESS,SES_PORT) as server:

                # securing using tls
                server.starttls(context=context)

                # authenticating with the server to prove our identity
                server.login(user=SES_USER_ID, password=SES_PASSWORD)

                # sending a plain text email
                server.sendmail(SES_FROM, SES_TO, email)
                
        else:
            print_message = f'No email sent as {message}'

        print(print_message)
        return print_message

if __name__ == '__main__':
    run_markets(test=True, test_rsi=0.5, test_mfi=0.6)