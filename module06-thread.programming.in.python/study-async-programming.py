import time
# import requests
import grequests

"""
def get_sync_ticker(symbol):
    return requests.get(url=f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}").content
"""


def get_async_ticker():
    return (grequests.get(url=f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}") for symbol in symbols)


symbols = [
    "LTCBTC", "BNBBTC", "NEOBTC", "BTCUSDT", "ETHUSDT"
]

"""
def sync_call():
    for symbol in symbols:
        ticker = get_sync_ticker(symbol)
        print(ticker)
"""


start = time.perf_counter()
for ticker in grequests.map(get_async_ticker()):
    print(ticker.content)
elapsed_time = time.perf_counter() - start
print(f"{elapsed_time:3.2f} seconds")
