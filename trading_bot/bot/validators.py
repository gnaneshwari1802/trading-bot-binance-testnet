VALID_SIDES = ["BUY", "SELL"]
VALID_TYPES = ["MARKET", "LIMIT"]


def validate_order(symbol, side, order_type, quantity, price=None):
    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must end with USDT.")

    if side.upper() not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL.")

    if order_type.upper() not in VALID_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT.")

    if float(quantity) <= 0:
        raise ValueError("Quantity must be greater than 0.")

    if order_type.upper() == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")

        if float(price) <= 0:
            raise ValueError("Price must be greater than 0.")