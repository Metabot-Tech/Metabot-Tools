import logging
import ccxt
from dynaconf import settings

logger = logging.getLogger(__name__)


class Trader(object):
    _pair = "{}/ETH"
    _LIMIT = "limit"

    def __init__(self):
        self.markets = {
            'LIQUI': ccxt.liqui({
                'apiKey': settings.LIQUI.API_KEY,
                'secret': settings.LIQUI.API_SECRET
            }),
            'BINANCE': ccxt.binance({
                'apiKey': settings.BINANCE.API_KEY,
                'secret': settings.BINANCE.API_SECRET
            })
        }

        # Init markets
        for key, value in self.markets.items():
            value.load_markets()

    def buy(self, market, coin, volume, rate):
        symbol = self._pair.format(coin)
        volume = self.markets.get(market).amount_to_lots(symbol, volume)
        return self.markets.get(market).create_order(symbol, self._LIMIT, 'buy', volume, rate)

    def sell(self, market, coin, volume, rate):
        symbol = self._pair.format(coin)
        volume = self.markets.get(market).amount_to_lots(symbol, volume)
        return self.markets.get(market).create_order(symbol, self._LIMIT, 'sell', volume, rate)

    def cancel_order(self, market, coin, order_id):
        symbol = self._pair.format(coin)
        return self.markets.get(market).cancel_order(order_id, symbol)

    def fetch_order(self, market, coin, order_id):
        symbol = self._pair.format(coin)
        return self.markets.get(market).fetch_order(order_id, symbol)

    def get_balance(self, market, params={}):
        return self.markets.get(market).fetch_balance(params=params)

    def fetch_rates(self, market, coin):
        return self.markets.get(market).fetch_ticker(coin)
