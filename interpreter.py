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

    def interpret(self, args):
        command = args.command

        if command == "balance":
            self._balance()
        elif command == "order":
            self._order_info(args.market, args.coin, args.order_id)
        else:
            logger.error("Unknown command: {}".format(command))

