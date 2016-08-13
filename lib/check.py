import math
import time
import datetime
import requests
import re
import hashlib
import logging
import os
from settings import *
from helpers import *
from exchange import exchange, market_instance


def checkInterface():

    haobtc, okcoin, huobi = market_instance(exchange)
    
    for e in [haobtc, okcoin, huobi] :
        try :
            print  e.market() , e.ticker()
        except:
            print e.market() ,'API Interface error'
            return False
    print 'Interface check passed'
    return True


def checkBalance():
    haobtc, okcoin, huobi = market_instance(exchange)

    try:
        haobtc_asset = json.loads(haobtc.accountInfo())
        okcoin_asset = json.loads(okcoin.accountInfo())
        #huobi_asset = json.loads(huobi.accountInfo())
    except:
        print 'check balance error'
        return False

    haobtc_btc = haobtc_asset['exchange_btc'] + haobtc_asset['exchange_frozen_btc'] > HAOBTC_BALANCE['BTC']
    haobtc_cny = haobtc_asset['exchange_cny'] + haobtc_asset['exchange_frozen_cny'] > HAOBTC_BALANCE['CNY']
    okcoin_btc = float(okcoin_asset['info']['funds']['free']['btc']) + float(okcoin_asset['info']['funds']['freezed']['btc'])> OKCOIN_BALANCE['BTC']
    okcoin_cny = float(okcoin_asset['info']['funds']['free']['cny']) + float( okcoin_asset['info']['funds']['freezed']['cny']) > OKCOIN_BALANCE['CNY']
    result = haobtc_btc and haobtc_cny and okcoin_btc and okcoin_cny

    print 'okcoin_btc' , ( float(okcoin_asset['info']['funds']['free']['btc']) + float(okcoin_asset['info']['funds']['freezed']['btc']) )
    print 'okcoin_cny' ,  ( float(okcoin_asset['info']['funds']['free']['cny']) + float( okcoin_asset['info']['funds']['freezed']['cny']))
    print 'check Balance result',result
    if not haobtc_btc:
        print 'Haobtc BTC is not sufficient'
    else:
        print 'Haobtc BTC balance pass'

    if not haobtc_cny:
        print 'Haobtc CNY is not sufficient'
    else:
        print 'Haobtc CNY balance pass'

    if not okcoin_btc:
        print 'Okcoin BTC is not sufficient'
    else:
        print 'Okcoin BTC balance pass'

    if not okcoin_cny:
        print 'Okcoin CNY is not sufficient'
    else:
        print 'Okcoin CNY balance pass'

    # CHECK HUOBI

    return result


def checkHermesDir():

    if not os.path.exists(DATA_DIR) :
        print 'Data directory does not exsit'
        print 'Creating directory ...'
        try :
            os.mkdir(DATA_DIR)
            print 'Data directory created'
        except:
            print 'Can\'t create directory in ~ . Program Exist.'
            return False
    else:
        print 'Data directory exsit. Continue ... '

    return True

 