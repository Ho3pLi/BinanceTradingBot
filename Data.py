from binance import AsyncClient, BinanceSocketManager
import pandas as pd
import sqlalchemy
import nest_asyncio

nest_asyncio.apply()

symbol = 'BTCUSDT'

engine = sqlalchemy.create_engine('sqlite:///'+symbol+'stream.db')

def createFrame(rs):
    df = pd.DataFrame([rs])
    df = df[['s', 'E', 'p']]
    df.columns = ['Symbol', 'Time', 'Price']

    df.Price = df.Price.astype(float)

    df.Time = pd.to_datetime(df.Time, unit='ms')

    return df

async def getData():
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    ts = bm.trade_socket(symbol)

    async with ts as tscm:
        while True:
            rs = await tscm.recv()
            df = createFrame(rs)
            df.to_sql(symbol, engine, if_exists='append', index='False')
            print(df)