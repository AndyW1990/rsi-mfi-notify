import os
import json


####### CONSTANTS #######
CANDLE_PERIOD = "1wk"
ROLLING_PERIOD = 14

####### VARIABLES #######
MARKETS = json.loads(os.environ['MARKETS'])

####### CREDENTIALS #######
SES_HOST_ADDRESS = os.environ.get("SES_HOST_ADDRESS")
SES_PORT = 587 # 25, 587 or 2587
SES_USERNAME = os.environ.get("SES_USERNAME")
SES_USER_ID = os.environ.get("SES_USER_ID")
SES_PASSWORD = os.environ.get("SES_PASSWORD")
SES_FROM = os.environ.get("SES_FROM")
SES_TO = json.loads(os.environ['SES_TO'])
