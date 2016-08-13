import math
import time
import datetime
import requests
import re
import hashlib
import logging
from lib.helpers import *
from settings import *
from lib.exchange import exchange, market_instance, market_all
from lib.action import *
from lib.trade2 import *
from lib.action import *

def test():
    e, o, h ,b = market_all(exchange)
    #print e.depth()
    #print e.ticker()
    #print e.depth()
    #print e.buy(6, 2889)
    #print o.accountInfo()
    #print e.historyInfo(10)
    #print e.cancelAll()
    #print e.accountInfo()
    #print e.ticker()
    #print o.accountInfo()
    #print e.ordersInfo()
    #print h.ticker()['ticker']['buy']
    #print o.ticker()['ticker']['buy']
    #print h.accountInfo()
    #print h.sell(0.01,3500)
    #print e.accountInfo()
    #print e.ledger(100)
    #print h.marketSell(0.02)
    #print h.ticker()
    #print e.accountInfo()
    #print e.sell(40,4222)
    #print e.hedge(ROBOT_ID,HEDGE_POS,HEDGE_LENGTH)


test()

