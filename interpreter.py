import logging
import pprint
from trader import Trader
from dynaconf import settings

logger = logging.getLogger(__name__)


class Interpreter(object):
    def __init__(self):
        self.trader = Trader()
        self.markets = settings.MARKETS
        self.coins = settings.COINS

    def _balance(self):
        try:
            balance_results = [self.trader.get_balance(i) for i in self.markets]
            balance = dict(zip(self.markets, balance_results))
        except:
            logger.exception("An error occurred when trying to fetch the balance")

        # Log
        totals = {key: 0 for key in self.coins}
        for market in self.markets:
            for coin in self.coins:
                balance_coin = balance.get(market).get(coin).get('free')
                totals[coin] += balance_coin
                logger.info("{}: {} {}".format(market, balance_coin, coin))

        for coin, volume in totals.items():
            logger.info("Total {}: {}".format(coin, volume))

    def _order_info(self, market, coin, order_id):
        order = self.trader.fetch_order(market.upper(), coin.upper(), order_id)
        logger.info("\n{}".format(pprint.pformat(order)))

    def _order_cancel(self, market, coin, order_id):
        cancellation = self.trader.cancel_order(market.upper(), coin.upper(), order_id)
        logger.info("\n{}".format(pprint.pformat(cancellation)))

    def _order_sell(self, market, coin, volume, rate):
        order = self.trader.sell(market.upper(), coin.upper(), volume, rate)
        logger.info("\n{}".format(pprint.pformat(order)))

    def _order_buy(self, market, coin, volume, rate):
        order = self.trader.buy(market.upper(), coin.upper(), volume, rate)
        logger.info("\n{}".format(pprint.pformat(order)))

    def _ticker(self, market, coin):
        ticker = self.trader.fetch_rates(market.upper(), coin.upper())
        logger.info("\n{}".format(ticker))

    def interpret(self, args):
        command = args.command

        if command == "balance":
            self._balance()
        elif command == "order":
            self._order_info(args.market, args.coin, args.order_id)
        elif command == "cancel":
            self._order_cancel(args.market, args.coin, args.order_id)
        elif command == "sell":
            self._order_sell(args.market, args.coin, args.volume, args.rate)
        elif command == "buy":
            self._order_buy(args.market, args.coin, args.volume, args.rate)
        elif command == "ticker":
            self._ticker(args.market, args.coin)
        else:
            logger.error("Unknown command: {}".format(command))

