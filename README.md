# Trading Bot

## Setup

```bash
pip install -r requirements.txt
```

## Configure API

Create a `.env` file:

```
API_KEY=YOUR_BINANCE_TESTNET_API_KEY
API_SECRET=YOUR_BINANCE_TESTNET_SECRET_KEY
```

## Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 150000
```
```
https://demo.binance.com/en/my/wallet/account/futures
```
```
https://demo.binance.com/en/my/settings/api-management
```
## Assumptions

- Binance USDT-M Futures Testnet
- Python 3.x
- Uses python-binance library
- Logs are stored in `logs/trading_bot.log`
