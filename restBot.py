import asyncio
from binance import AsyncClient, BinanceSocketManager
import pandas as pd
import sqlalchemy
import secret
import nest_asyncio

nest_asyncio.apply()

symbol = 'BTC/USDT'

engine = sqlalchemy.create_engine('sqlite:///'+symbol+'stream.db')