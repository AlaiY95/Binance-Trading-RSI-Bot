# Binance-Trading-RSI-Bot

This is a trading bot for Binance Exchange using Relative Strength Index (RSI) indicator for sell and buy orders. 

The RSI is calculated using the last 14 recent close values. If the RSI is over 70 we will sell our Assets as this indicates the maket is overbought. If the RSI is lower than 30 we will buy ETH, because the market is oversold. The default crypto currency used is 'ETH' (Ethereum).

## DISCLAIMER
This project is for educational purpose!
I am not responsible for the trades you make with the script, this script has not been extensively tested on live trades.

## Setup

## Install Packages
Run:
```
pip install requirements.txt
```

For MacOs users you may run this command before installing the package `TA-lib`:
```
brew install ta-lib
```

## Config Variables
### API Credentials

1. [Signup](https://www.binance.com/de/register?ref=17026971) for Binance
2. Go to the API Center and create a new API key
```
[✓] Read Info [✓] Enable Trading [X] Enable Withdrawals
```

3. Insert your key and secret into ``config.py``

## Docs

* [Binance API](https://python-binance.readthedocs.io/en/latest/binance.html)
* [Websocket-Stream](https://github.com/binance-exchange/binance-official-api-docs/blob/master/web-socket-streams.md)
* [Original Github Code] Original Github code: https://github.com/hackingthemarkets/binance-tutorials]
