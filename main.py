from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime

API_KEY = "PK7HN5O32G19EHLY2XNF"
API_SECRET = "roWnv3LSxfd16R3fYtV0IzNPHxrwx53C5"
BASE_URL = "https://paper-api.alpaca.markets/v2"

ALPACA_CREDENTIAL = {
    "API_KEY": API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True
}

class MLTrader(Strategy):
    def init(self):
        pass

    def on_trading_iteration(self):
        return super().on_trading_iteration()

start_date = datetime(2023,12,15)
end_date = datetime(2023,12,31)
broker =  Alpaca(ALPACA_CREDENTIAL)
strategy = MLTrader(name='mlstrat', broker=broker, parameters={})

strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters={}
)