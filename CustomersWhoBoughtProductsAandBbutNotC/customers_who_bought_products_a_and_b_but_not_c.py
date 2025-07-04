def find_customers_who_bought_A_and_B_but_not_C(purchases):
    """
    Identifies customers who bought product 'A' and product 'B' but did not buy product 'C'.

    Args:
        purchases (list of tuple): A list where each tuple represents a purchase
                                   in the format (customer_id, product_id).

    Returns:
        list: A sorted list of customer IDs who meet the criteria.
    """
    customer_products = {}
    for customer_id, product_id in purchases:
        if customer_id not in customer_products:
            customer_products[customer_id] = set()
        customer_products[customer_id].add(product_id)

    result_customers = []
    for customer_id, products_set in customer_products.items():
        bought_A = 'A' in products_set
        bought_B = 'B' in products_set
        bought_C = 'C' in products_set

        if bought_A and bought_B and not bought_C:
            result_customers.append(customer_id)
            
    result_customers.sort() 
    return result_customers

if __name__ == "__main__":
    # Example usage:
    sample_purchases = [
        (1, 'A'), (1, 'B'), (1, 'D'),
        (2, 'A'), (2, 'B'), (2, 'C'),
        (3, 'A'), (3, 'B'), (3, 'E'),
        (4, 'A'), (4, 'F'),
        (5, 'B'), (5, 'A'), (5, 'E'),
        (6, 'X'), (6, 'Y'),
        (7, 'A'), (7, 'C'),
        (8, 'B'), (8, 'C'),
        (9, 'A'), (9, 'B'), (9, 'C'), (9, 'D'), # Bought A, B, C
        (10, 'A'), (10, 'B'),
        (11, 'A'),
        (12, 'B'),
    ]

    customers = find_customers_who_bought_A_and_B_but_not_C(sample_purchases)
    print(customers) # Expected output: [1, 3, 5, 10]
    
    # Another example with no matching customers
    no_match_purchases = [
        (1, 'A'), (1, 'C'),
        (2, 'B'), (2, 'C'),
    ]
    customers_no_match = find_customers_who_bought_A_and_B_but_not_C(no_match_purchases)
    print(customers_no_match) # Expected output: []

    # Example with empty purchases list
    empty_purchases = []
    customers_empty = find_customers_who_bought_A_and_B_but_not_C(empty_purchases)
    print(customers_empty) # Expected output: []