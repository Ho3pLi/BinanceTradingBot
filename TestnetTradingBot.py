from binance.client import Client
from dotenv import load_dotenv
import os
import time

load_dotenv()

api_key = os.getenv("TESTNET_API_KEY")
api_secret = os.getenv("TESTNET_API_SECRET")

symbol = 'BTCUSDT'
short_sma_period = 5
long_sma_period = 10
investment_amount = 10

client = Client(api_key, api_secret)

def getClosingPrice(symbol):
    ticker = client.get_ticker(symbol=symbol)
    return float(ticker['lastPrice'])

def calculateSMA(symbol, period):
    klines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1MINUTE, f"{period} day ago UTC")
    closes = [float(data[4]) for data in klines]
    return sum(closes) / len(closes)

# SMA indicator based strategy, scalping strategy
def letsGetPoor():
    position = 'out'
    invested_amount = 0

    while True:
        closing_price = getClosingPrice(symbol)

        short_sma = calculateSMA(symbol, short_sma_period)
        long_sma = calculateSMA(symbol, long_sma_period)

        if position == 'out':
            if closing_price < short_sma and closing_price < long_sma:
                invested_amount = investment_amount
                position = 'in'
                print('Segnale di acquisto')
        elif position == 'in':
            if closing_price > short_sma and closing_price > long_sma:
                invested_amount = 0
                position = 'out'
                print('Segnale di vendita')

        print(f'Prezzo di chiusura: {closing_price}')
        print(f'Short SMA: {short_sma}')
        print(f'Long SMA: {long_sma}')
        print(f'Posizione: {position}')
        print(f'Capitale: {investment_amount}')
        print('-------------------------')

        if invested_amount >= 100:
            break

        time.sleep(10)

letsGetPoor()