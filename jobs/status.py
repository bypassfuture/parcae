import sys,os
import time
import datetime
import psycopg2
import requests
import random
sys.path.append(".")
from lib.exchange import exchange, market_instance
from settings import *


wait = 40

while True:

    time.sleep(wait)