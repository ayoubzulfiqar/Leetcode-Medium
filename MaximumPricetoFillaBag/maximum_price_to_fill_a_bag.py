def max_price_to_fill_bag(items, capacity):
    item_details = []
    for price, weight in items:
        if weight > 0:
            item_details.append((price / weight, price, weight))

    item_details.sort(key=lambda x: x[0], reverse=True)

    total_price = 0.0
    remaining_capacity = float(capacity)

    for price_per_unit, price, weight in item_details:
        if remaining_capacity <= 0:
            break

        if weight <= remaining_capacity:
            total_price += price
            remaining_capacity -= weight
        else:
            fraction = remaining_capacity / weight
            total_price += price * fraction
            remaining_capacity = 0
            break

    return total_price