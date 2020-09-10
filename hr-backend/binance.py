import time

import requests
import schedule


def call_binance_for_ticker():
    resp = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    print(resp.json())


schedule.every(1).seconds.do(call_binance_for_ticker)

while 1:
    schedule.run_pending()
    time.sleep(1)
