import datetime

def get_most_recent_orders(orders):
    most_recent_orders = {}
    for order in orders:
        product_id = order['product_id']
        current_timestamp = datetime.datetime.strptime(order['timestamp'], '%Y-%m-%d %H:%M:%S')

        if product_id not in most_recent_orders:
            most_recent_orders[product_id] = order
        else:
            stored_order = most_recent_orders[product_id]
            stored_timestamp = datetime.datetime.strptime(stored_order['timestamp'], '%Y-%m-%d %H:%M:%S')
            if current_timestamp > stored_timestamp:
                most_recent_orders[product_id] = order
    return most_recent_orders

if __name__ == "__main__":
    orders_data = [
        {"order_id": 1, "product_id": "A", "timestamp": "2023-01-01 10:00:00"},
        {"order_id": 2, "product_id": "B", "timestamp": "2023-01-01 11:00:00"},
        {"order_id": 3, "product_id": "A", "timestamp": "2023-01-01 12:00:00"},
        {"order_id": 4, "product_id": "C", "timestamp": "2023-01-01 09:00:00"},
        {"order_id": 5, "product_id": "B", "timestamp": "2023-01-01 10:30:00"},
        {"order_id": 6, "product_id": "A", "timestamp": "2023-01-01 11:30:00"},
        {"order_id": 7, "product_id": "D", "timestamp": "2023-01-01 15:00:00"},
        {"order_id": 8, "product_id": "D", "timestamp": "2023-01-01 14:00:00"},
        {"order_id": 9, "product_id": "E", "timestamp": "2023-01-01 08:00:00"},
    ]

    result = get_most_recent_orders(orders_data)
    print(result)