import argparse
import os
import logging
from interpreter import Interpreter

logging.basicConfig(format="%(asctime)s %(name)-40s %(levelname)-8s %(message)s", level=logging.INFO)


def main():
    # Settings
    os.environ['DYNACONF_SETTINGS'] = "settings.yml"

    # Parse arguments
    parser = argparse.ArgumentParser(description='Tool to manipulate accounts')
    subparsers = parser.add_subparsers(help='command help', dest='command')

    parser_balance = subparsers.add_parser('balance', help='balance help')

    parser_order = subparsers.add_parser('order', help='order help')
    parser_order.add_argument("market", action='store')
    parser_order.add_argument("coin", action='store')
    parser_order.add_argument("order_id", action='store')

    parser_order = subparsers.add_parser('cancel', help='cancel help')
    parser_order.add_argument("market", action='store')
    parser_order.add_argument("coin", action='store')
    parser_order.add_argument("order_id", action='store')

    parser_order = subparsers.add_parser('sell', help='sell help')
    parser_order.add_argument("market", action='store')
    parser_order.add_argument("coin", action='store')
    parser_order.add_argument("volume", action='store', type=float)
    parser_order.add_argument("rate", action='store', type=float)

    parser_order = subparsers.add_parser('buy', help='buy help')
    parser_order.add_argument("market", action='store')
    parser_order.add_argument("coin", action='store')
    parser_order.add_argument("volume", action='store', type=float)
    parser_order.add_argument("rate", action='store', type=float)

    args = parser.parse_args()

    # Interpret command
    interpreter = Interpreter()
    interpreter.interpret(args)

if __name__ == '__main__':
    main()
