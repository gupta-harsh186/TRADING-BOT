def validate_order(symbol, side, order_type, quantity, price):
    if not symbol:
        raise ValueError("Symbol required")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid order type")

    if quantity <= 0:
        raise ValueError("Quantity must be > 0")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT order")
    
    if quantity * (price if price else 70000) < 100:
         raise ValueError("Order value must be at least 100 USDT")