import datetime

class OrderManager:
    def __init__(self):
        self.orders = []
        self.next_order_id = 1

    def add_order(self, timestamp=None):
        if timestamp is None:
            timestamp = datetime.datetime.now()
        
        order = {
            'order_id': self.next_order_id,
            'timestamp': timestamp
        }
        self.orders.append(order)
        self.next_order_id += 1
        return order

    def get_most_recent_three_orders(self):
        sorted_orders = sorted(self.orders, key=lambda x: x['timestamp'], reverse=True)
        return sorted_orders[:3]