# Metabot-Tools

This is a collection of tools for the [artis bot](https://github.com/Metabot-Tech/artis). Some of the code was copied from there so you can expect some legacy code.

Usage `python app.py {COMMAND}`

The available commands are:
- `balance`: Will get you the balance for each coin on each market
- `ticker {MARKET} {PAIR}`: Will get you the current ticker for the specified market and pair
- `sell {MARKET} {COIN} {AMOUNT} {PRICE}`: Places a sell order at the specified market
- `buy {MARKET} {COIN} {AMOUNT} {PRICE}`: Places a buy order at the specified market
- `order {MARKET} {COIN} {ORDER_ID}`: Get information about an order
- `cancel {MARKET} {COIN} {ORDER_ID}`: Cancel an active order

# Setup
As for the bot, you will a `settings.yml` file with the following information:

```yaml
DYNACONF:
    MARKETS: ['LIQUI', 'BINANCE']
    COINS: ['ETH', 'TRX', 'WAVES']
    LIQUI:
        COINS: ['ADX', 'TRX']
        API_KEY: <API KEY HERE>
        API_SECRET: <API SECRET HERE>
    BINANCE:
        COINS: ['ADX', 'TRX']
        API_KEY: <API KEY HERE>
        API_SECRET: <API SECRET HERE>
```
