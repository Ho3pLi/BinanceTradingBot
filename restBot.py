import asyncio
from binance import AsyncClient, BinanceSocketManager
import pandas as pd
import sqlalchemy
import secret
import nest_asyncio

nest_asyncio.apply()

symbol = 'BTCUSDT'

engine = sqlalchemy.create_engine('sqlite:///'+symbol+'stream.db')

async def getData():
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    ts = bm.trade_socket(symbol)

    async with ts as tscm:
        while True:
            rs = await tscm.recv()
            print(rs)