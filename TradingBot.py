import sqlalchemy
import pandas as pd
from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

client = Client(api_key=api_key, api_secret=api_secret)
symbol = 'BTCUSDT'
engine = sqlalchemy.create_engine('sqlite:///'+symbol+'stream.db')
df = pd.read_sql(symbol, engine)
print(df)

# Define here your strategy