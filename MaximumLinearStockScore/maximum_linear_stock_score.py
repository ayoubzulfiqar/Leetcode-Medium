import math

def max_linear_stock_score(prices):
    if not prices or len(prices) < 2:
        return 0

    min_price = math.inf
    max_profit = 0

    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
            
    return max_profit