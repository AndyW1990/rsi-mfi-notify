import os

import pytest
import unittest
from app.main import run_markets

class TestVals(unittest.TestCase):
         
    def test_buy(self):
        rsi = 90
        mfi = 70
        market = 'SPY'
        email_message = f'{market} is overbought, sell a percentage of stock! \nRSI = {rsi:.1f} \nMFI = {mfi:.1f}'
        print_message = f'Sending email as {email_message}'
        self.assertEqual(run_markets(test=True, test_rsi=rsi, test_mfi=mfi, use_send=False), print_message)
    
    def test_sell(self):
        rsi = 30
        mfi = 50
        market = 'SPY'
        email_message = f'{market} is oversold, consider buying some stock. \nRSI = {rsi:.1f} \nMFI = {mfi:.1f}'
        print_message = f'Sending email as {email_message}'
        self.assertEqual(run_markets(test=True, test_rsi=rsi, test_mfi=mfi, use_send=False), print_message)
        
    def test_do_nothing_1(self):
        rsi = 60
        mfi = 60
        market = 'SPY'
        email_message = f'{market} is neither oversold nor overbought. \nRSI = {rsi:.1f} \nMFI = {mfi:.1f}'
        print_message = f'No email sent as {email_message}'
        self.assertEqual(run_markets(test=True, test_rsi=rsi, test_mfi=mfi, use_send=False), print_message)
        
    def test_do_nothing_2(self):
        rsi = 60
        mfi = 80
        market = 'SPY'
        email_message = f'{market} is neither oversold nor overbought. \nRSI = {rsi:.1f} \nMFI = {mfi:.1f}'
        print_message = f'No email sent as {email_message}'
        self.assertEqual(run_markets(test=True, test_rsi=rsi, test_mfi=mfi, use_send=False), print_message)
        
    def test_do_nothing_3(self):
        rsi = 80
        mfi = 30
        market = 'SPY'
        email_message = f'{market} is neither oversold nor overbought. \nRSI = {rsi:.1f} \nMFI = {mfi:.1f}'
        print_message = f'No email sent as {email_message}'
        self.assertEqual(run_markets(test=True, test_rsi=rsi, test_mfi=mfi, use_send=False), print_message)
    
    