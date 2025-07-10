import datetime

def immediate_food_delivery_iii(orders):
    customer_stats = {}

    for order in orders:
        customer_id = order['customer_id']
        order_date_str = order['order_date']
        pref_delivery_date_str = order['customer_pref_delivery_date']

        order_date = datetime.datetime.strptime(order_date_str, '%Y-%m-%d').date()
        pref_delivery_date = datetime.datetime.strptime(pref_delivery_date_str, '%Y-%m-%d').date()

        if customer_id not in customer_stats:
            customer_stats[customer_id] = {'total_orders': 0, 'immediate_orders': 0}

        customer_stats[customer_id]['total_orders'] += 1

        if order_date == pref_delivery_date:
            customer_stats[customer_id]['immediate_orders'] += 1

    result = []
    for customer_id, stats in customer_stats.items():
        total_orders = stats['total_orders']
        immediate_orders = stats['immediate_orders']

        percentage = (immediate_orders / total_orders) * 100.0

        result.append({
            'customer_id': customer_id,
            'immediate_percentage': round(percentage, 2)
        })
    
    # Sort by customer_id for consistent output, as is common in such problems
    result.sort(key=lambda x: x['customer_id'])

    return result

if __name__ == "__main__":
    # Sample input data based on common problem examples
    orders_data = [
        {'delivery_id': 1, 'customer_id': 1, 'order_date': '2019-08-01', 'customer_pref_delivery_date': '2019-08-02'},
        {'delivery_id': 2, 'customer_id': 2, 'order_date': '2019-08-02', 'customer_pref_delivery_date': '2019-08-02'},
        {'delivery_id': 3, 'customer_id': 1, 'order_date': '2019-08-11', 'customer_pref_delivery_date': '2019-08-11'},
        {'delivery_id': 4, 'customer_id': 3, 'order_date': '2019-08-24', 'customer_pref_delivery_date': '2019-08-24'},
        {'delivery_id': 5, 'customer_id': 3, 'order_date': '2019-08-21', 'customer_pref_delivery_date': '2019-08-22'},
        {'delivery_id': 6, 'customer_id': 2, 'order_date': '2019-08-11', 'customer_pref_delivery_date': '2019-08-13'},
        {'delivery_id': 7, 'customer_id': 4, 'order_date': '2019-08-11', 'customer_pref_delivery_date': '2019-08-11'}
    ]

    output = immediate_food_delivery_iii(orders_data)
    print(output)