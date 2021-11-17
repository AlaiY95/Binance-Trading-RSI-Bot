import json
import websocket
import numpy as np
import talib
from pprint import pprint
from binance.client import Client
from binance.enums import *
import config

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

#RSI Setup
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = "ETHUSD"
TRADE_QUANTITY = 0.05

closes_price =[]
in_position = False

client = Client(config.API_KEY, config.API_Secret, tld="de")

def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        print("sending order")
        order = client.create_order(symbol=symbol,
                                side=side,
                                type=order_type,
                                quantity=quantity)
        print(order)
    except Exception as e:
        print("An exception occured - {}".format(e))
        return False

    return True

def on_open(ws):
    print('Open connection')

def on_close(ws):
    print('Close connection')

def on_message(ws, message):
    global closes_price, in_position

    print('Received')
    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle = json_message['k']
    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        #print("candle closed at {}".format(close))
        closes_price.append(float(close))
        print("closes" + closes_price)

        if len(closes_price) > RSI_PERIOD:
            np_closes = numpy.array(closes_price)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("all rsis calculated so far")
            print(rsi)
            last_rsi = rsi[-1]

            if last_rsi > RSI_OVERBOUGHT:
                if in_position:
                    print("Overbought! SELL! SELL! SELL!")
                    # Binance sell order logic here
                    order_succeeded = order(SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)
                    if order_succeeded:
                        in_position = False
                else:
                    print("It is overbought, but you don't own any. Nothing to do.")

            if last_rsi < RSI_OVERSOLD:
                if in_position:
                    print("It is oversold, but you already own it, nothing  to do.")
                else:
                    print("Oversold! BUY! BUY! BUY")
                    # Binance buy order logic here
                    order_succeeded = order(SIDE_BUY, TRADE_QUANTITY, TRADE_SYMBOL)
                    if order_succeeded:
                        in_position = True


ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()