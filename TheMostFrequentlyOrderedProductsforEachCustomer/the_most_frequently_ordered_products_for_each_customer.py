import collections

def get_most_frequently_ordered_products(orders):
    customer_product_counts = collections.defaultdict(collections.Counter)

    for customer_id, product_id in orders:
        customer_product_counts[customer_id][product_id] += 1

    result = {}

    for customer_id, product_counts in customer_product_counts.items():
        max_freq = product_counts.most_common(1)[0][1]
        
        most_frequent_products = []
        for product, count in product_counts.items():
            if count == max_freq:
                most_frequent_products.append(product)
        
        most_frequent_products.sort()
        result[customer_id] = most_frequent_products
    
    return result