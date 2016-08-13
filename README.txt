HAOBTC  Market Maker System v0.01

Requirements : python 2.7 / postgresql / haobtc okcoin huobi account API 

Install 


sudo apt-get install -y  postgresql postgresql-contrib build-essential libpq-dev python-dev python3-dev


pip install -r requirements.txt

psql -c 'create database hermes owner db_user'

python install.py

--------------------------

Supervise Two processes 

1.main process

python main.py

2.arbitrage process

python jobs/arbitrage.py