import sys, getopt
import time
sys.path.append(".")
from lib.exchange import exchange,market_instance
from lib.trade2 import get_unhedged
from lib.action import getMarketPrice

def main():
    if len(sys.argv) == 1:
        print 'Parcae command tools, usage : python bin/supervise.py args '
        print '1.cancelall 2.status 3.check 4.market_balance'
    else:
        
        haobtc, okcoin, huobi = market_instance(exchange)

        if sys.argv[1] == 'cancel':
            haobtc.cancelAll()

        if sys.argv[1] == 'depth':
 
            pass

        if sys.argv[1] == 'check':
            pass

        if sys.argv[1] == 'market_balance':
            pass

        if sys.argv[1] == 'price':
            pass
    return


if __name__ == "__main__":    
    main()
