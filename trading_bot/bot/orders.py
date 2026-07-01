from binance.enums import *
from bot.client import get_client
from bot.logging_config import setup_logger

logger = setup_logger()


def place_order(symbol, side, order_type, quantity, price=None):

    client = get_client()

    try:

        logger.info(
            f"Request: {side} {quantity} {symbol} {order_type}"
        )

        if order_type.upper() == "MARKET":

            order = client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type=FUTURE_ORDER_TYPE_MARKET,
                quantity=quantity
            )

        else:

            order = client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type=FUTURE_ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=str(price),
                timeInForce=TIME_IN_FORCE_GTC
            )

        logger.info(order)

        print("\n========== ORDER SUCCESS ==========")
        print("Order ID :", order["orderId"])
        print("Status   :", order["status"])
        print("Executed :", order["executedQty"])
        print("Avg Price:", order.get("avgPrice", "N/A"))
        print("===================================")

    except Exception as e:

        logger.error(str(e))
        print("\nOrder Failed")
        print(e)