import math
import time
import datetime
import requests
import re
import hashlib
import logging
import curses
from settings import *
from lib.strategy import *

def main():
 
    # ....
    result_pass = initHermes()
    tactic = strategy()
    level = RISK_LEVEL
    if not True:
        print 'Conditions does not allow Hermes to start '
        return
    else:
        print 'Hermes started ! Risk level %(level)s Good luck! ' % {'level':level}

    while True:
        tactic.provideLiquidity(level)
        time.sleep(HERMES_INTERVAL)


if __name__ == '__main__':
    main()