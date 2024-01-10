import os

import pytest
import unittest
from main import run_markets

class TestVals(unittest.TestCase):
         
    def test_buy(self):
        rsi = 0.9
        mfi = 0.7
        market = 'SPY'
        email_message = f'{market} is overbought, sell a percentage of stock! \nRSI = {rsi:.2f} \nMFI = {mfi:.2f}'
        print_message = f'Sending email as {email_message}'
        self.assertEqual(run_markets(test=True, test_rsi=rsi, test_mfi=mfi), print_message)
    
    def test_sell(self):
        rsi = 0.3
        mfi = 0.5
        market = 'SPY'
        email_message = f'{market} is oversold, consider buying some stock. \nRSI = {rsi:.2f} \nMFI = {mfi:.2f}'
        print_message = f'Sending email as {email_message}'
        self.assertEqual(run_markets(test=True, test_rsi=rsi, test_mfi=mfi), print_message)
        
    def test_do_nothing_1(self):
        rsi = 0.6
        mfi = 0.6
        market = 'SPY'
        email_message = f'{market} is neither oversold nor overbought. \nRSI = {rsi:.2f} \nMFI = {mfi:.2f}'
        print_message = f'No email sent as {email_message}'
        self.assertEqual(run_markets(test=True, test_rsi=rsi, test_mfi=mfi), print_message)
        
    def test_do_nothing_2(self):
        rsi = 0.6
        mfi = 0.8
        market = 'SPY'
        email_message = f'{market} is neither oversold nor overbought. \nRSI = {rsi:.2f} \nMFI = {mfi:.2f}'
        print_message = f'No email sent as {email_message}'
        self.assertEqual(run_markets(test=True, test_rsi=rsi, test_mfi=mfi), print_message)
        
    def test_do_nothing_3(self):
        rsi = 0.8
        mfi = 0.3
        market = 'SPY'
        email_message = f'{market} is neither oversold nor overbought. \nRSI = {rsi:.2f} \nMFI = {mfi:.2f}'
        print_message = f'No email sent as {email_message}'
        self.assertEqual(run_markets(test=True, test_rsi=rsi, test_mfi=mfi), print_message)
    
    