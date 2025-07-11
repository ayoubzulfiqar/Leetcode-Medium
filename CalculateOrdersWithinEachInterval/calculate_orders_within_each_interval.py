def calculate_orders_within_intervals(orders, intervals):
    results = []
    for interval_start, interval_end in intervals:
        count = 0
        for order_start, order_end, _ in orders:
            if interval_start <= order_start and order_end <= interval_end:
                count += 1
        results.append(count)
    return results