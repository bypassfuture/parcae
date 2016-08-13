import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)


HAOBTC_API_KEY = ' '
HAOBTC_SECRET_TOKEN = ''
HAOBTC_API_URL = {
                  'host' :'www.haobtc.com',
                  'trade':'https://haobtc.com/exchange/api/v1/trade',
                  'cancel_order':'https://haobtc.com/exchange/api/v1/cancel_order',
                  'order_info':'https://haobtc.com/exchange/api/v1/order_info',
                  'orders_info':'https://haobtc.com/exchange/api/v1/orders_info',
                  'history_info':'https://haobtc.com/exchange/api/v1/history_info',
                  'account_info':'https://haobtc.com/exchange/api/v1/account_info',
                  'ticker':'https://haobtc.com/exchange/api/v1/ticker' ,
                  'depth':'https://haobtc.com/exchange/api/v1/depth',
                  'batch_trade':'https://haobtc.com/exchange/api/v1/batch_trade',
                  'cancel_all':'https://haobtc.com/exchange/api/v1/cancel_all',
                  'cancel_list':'https://haobtc.com/exchange/api/v1/cancel_list',
                  'fast_ticker':'https://haobtc.com/api/v1/price/cny',
                  'ledger':'https://haobtc.com/exchange/api/v1/ledger',
                  'hedge':'https://haobtc.com/exchange/api/v1/hedge'
                  }
HAOBTC_BALANCE = {'BTC':50,'CNY':100000}
HAOBTC_API = {'fee':0.001}

#haobtc hermes account
HUOBI_API_KEY = ''
HUOBI_SECRET_TOKEN = ''

# test account
HUOBI_API_URL = {
                  'host':'api.huobi.com/apiv3',
                  'ticker':'http://api.huobi.com/staticmarket/ticker_btc_json.js',
                  'depth':'http://api.huobi.com/staticmarket/depth_btc_json.js',
                  'data':'http://api.huobi.com/staticmarket/detail_btc_json.js',
                  'buy' : 'buy',
                  'buy_market':  'buy_market',
                  'cancel_order': 'cancel_order',
                  'account_info': 'get_account_info',
                  'new_deal_orders': 'get_new_deal_orders',
                  'order_id_by_trade_id': 'get_order_id_by_trade_id',
                  'get_orders': 'get_orders',
                  'order_info': 'order_info',
                  'sell': 'sell',
                  'sell_market': 'sell_market',
                }

HUOBI_BALANCE = {'BTC':0,'CNY':0}

OKCOIN_API_KEY = ''
OKCOIN_SECRET_TOKEN = ''
OKCOIN_API_URL = {
                   'host':'www.okcoin.cn',
                   'ticker': 'https://www.okcoin.cn/api/v1/ticker.do',
                   'depth': 'https://www.okcoin.cn/api/v1/depth.do',
                   'tradesInfo':'https://www.okcoin.cn/api/v1/trades.do',
                   'userInfo':'https://www.okcoin.cn/api/v1/userinfo.do',
                   'trade':'https://www.okcoin.cn/api/v1/trade.do',
                   'batch_trade':'https://www.okcoin.cn/api/v1/batch_trade.do',
                   'cancel_order':'https://www.okcoin.cn/api/v1/cancel_order.do',
                   'order_info':'https://www.okcoin.cn/api/v1/order_info.do',
                   'order_history':'https://www.okcoin.cn/api/v1/order_history.do'
                }

OKCOIN_BALANCE = {'BTC':0.2,'CNY':200}
OKCOIN_MIN_TRADE = {'buy':0.01,'sell':0.01 , 'trade':0.01}
OKCOIN_API = {'max_open_order':50,'fee':0.004}

BTCC_API_KEY = ''
BTCC_SECRET_TOKEN = ''
BTCC_API_URL = {
                  'host': 'data.btcchina.com',
                  'ticker':'https://data.btcchina.com/data/ticker'
                  }


#TRADING SETTINGS
ARBITRAGE_INTERVAL = 2 #arbitrage time interval / python jobs/arbitrager.py
TOTAL = {'BTC':200,'CNY':300000} # ALL ASSEST =  HAOBTC + HUOBI + OKCOIN +...
ORDER_LIST_WEIGHT = {'okcoin':0.1 , 'huobi':0.1} # DEPTH ORDERS WEIGHT
TRADE_WEIGHT = {'mode':'single', 'okcoin':1, 'huobi':0} # HEDGE TRADE SIZE WEIGHT ,all / single / multi
RISK_RATE = 0.7 # MAX RISK AMOUNT = RISK_RATE * HAOBTC_BALANCE[CURRENCY]
LARGER_DEPTH = {'provide':True,'deep':8,'random':True, 'max_value': 1 ,'step':4}
LARGE_ORDER_POS = 3  # larger order position (askX, bidX)
HERMES_INTERVAL = 7
TREND = {'normal':{'buy':0,'sell':0},'up':{'buy':-5,'sell':5},'down':{'buy':-10,'sell':0}}
HEDGE_STRICT = True
EAT_ORDER = {'min':1,'max':100,'gap':20}
NORMAL_SIZE=15
TRADE_HISTORY = 20
HEDGE_LENGTH = 2000000
HEDGE_TIME = 20 
HEDGE_POS = 13019459
MOCK_TRADE = {"mock":True, "depth":10,"max_order":1,"min_order":0.01}
HUOBI_OKCOIN_PREMIUM = 30
ORDER_SLICE={'T':5,'L':4}
ROBOT_ID = {'id':[45645 , 49158 , 50000, 19447]}

#STRATEGY SETTINGS
STRATEGY = 'maker_taker' # ['none','marker_taker','pos_depth']
ALL_MAKER = False
DEFAULT_MAKER_DEPTH = 32 #
EXCHANGE_LEADER = 'okcoin'

ORDER_PRICE_INTERVAL = range(100)
RISK_LEVEL = 0 # 0-9 / lower value higher risk , 0 is the highest risk. The more risk more liquidity

MAX_PRICE_INTERVAL_RATE = 0.05
MIN_PRICE_INTERVAL_RATE = 0

MARKER_ORDER_POSITION = 0 # set to 0 could provide more liquidity
TAKER_ORDER_POSITION = -1 # set to -1 could provide more liquidity

#ROBOT OPTIONS
ROBOT_MAX_BUY = 1
USE_ROBOT = True
ROBOT_TRADE_INTERVAL =39


#DATA DIR & DATABASE
DATA_DIR = os.path.expanduser('~') + '/.hermes'

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'password'
DB_NAME = 'hermes'

#IMPORT local_settings
try:
    from local_settings import *
except ImportError:
    pass

