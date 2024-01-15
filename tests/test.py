import os

import pytest
import unittest
from app.main import run_markets

class TestVals(unittest.TestCase):
         
    def test_buy(self):
        rsi = 90
        mfi = 70
        market = '^SPX'
        email_message = f'{market} is overbought, sell a percentage of stock! \nRSI = {rsi:.1f} \nMFI = {mfi:.1f}'
        self.assertEqual(run_markets(test=True, test_market=market, test_rsi=rsi, test_mfi=mfi, use_send=False), email_message)
    
    def test_sell(self):
        rsi = 30
        mfi = 50
        market = '^SPX'
        email_message = f'{market} is oversold, consider buying some stock. \nRSI = {rsi:.1f} \nMFI = {mfi:.1f}'
        self.assertEqual(run_markets(test=True, test_market=market, test_rsi=rsi, test_mfi=mfi, use_send=False), email_message)
        
    def test_do_nothing_1(self):
        rsi = 60
        mfi = 60
        market = '^SPX'
        email_message = f'{market} is neither oversold nor overbought. \nRSI = {rsi:.1f} \nMFI = {mfi:.1f}'
        self.assertEqual(run_markets(test=True, test_market=market, test_rsi=rsi, test_mfi=mfi, use_send=False), email_message)
        
    def test_do_nothing_2(self):
        rsi = 60
        mfi = 80
        market = '^SPX'
        email_message = f'{market} is neither oversold nor overbought. \nRSI = {rsi:.1f} \nMFI = {mfi:.1f}'
        self.assertEqual(run_markets(test=True, test_market=market, test_rsi=rsi, test_mfi=mfi, use_send=False), email_message)
        
    def test_do_nothing_3(self):
        rsi = 80
        mfi = 30
        market = '^SPX'
        email_message = f'{market} is neither oversold nor overbought. \nRSI = {rsi:.1f} \nMFI = {mfi:.1f}'
        self.assertEqual(run_markets(test=True, test_market=market, test_rsi=rsi, test_mfi=mfi, use_send=False), email_message)
    
class TestEmail(unittest.TestCase):
     def test_buy(self):
        rsi = 90
        mfi = 70
        market = '^SPX'
        email_message = f'{market} is overbought, sell a percentage of stock! \nRSI = {rsi:.1f} \nMFI = {mfi:.1f}'
        self.assertEqual(run_markets(test=True, test_market=market, test_rsi=rsi, test_mfi=mfi, use_send=True), email_message)
    
