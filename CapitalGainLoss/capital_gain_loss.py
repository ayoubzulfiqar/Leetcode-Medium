from collections import defaultdict

def calculate_capital_gain_loss(stocks_table):
    grouped_stocks = defaultdict(list)
    for row in stocks_table:
        grouped_stocks[row["stock_name"]].append(row)

    result = []
    for stock_name, operations in grouped_stocks.items():
        operations.sort(key=lambda x: x["operation_day"])

        current_gain_loss = 0
        buy_price = 0

        for op in operations:
            if op["operation"] == "Buy":
                buy_price = op["price"]
            elif op["operation"] == "Sell":
                current_gain_loss += (op["price"] - buy_price)

        result.append({"stock_name": stock_name, "capital_gain_loss": current_gain_loss})
    
    return result