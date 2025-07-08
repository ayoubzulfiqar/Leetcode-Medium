def get_orders_with_max_quantity_above_average(orders):
    if not orders:
        return []

    total_quantity = 0
    max_quantity = -float('inf')

    for order in orders:
        quantity = order['quantity']
        total_quantity += quantity
        if quantity > max_quantity:
            max_quantity = quantity

    average_quantity = total_quantity / len(orders)

    result_orders = []
    for order in orders:
        if order['quantity'] == max_quantity and order['quantity'] > average_quantity:
            result_orders.append(order)

    return result_orders