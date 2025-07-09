import collections

def calculate_salesperson_influence(transactions):
    salesperson_customers = collections.defaultdict(set)
    for salesperson_id, customer_id in transactions:
        salesperson_customers[salesperson_id].add(customer_id)
    salesperson_influence = {}
    for salesperson_id, customers_set in salesperson_customers.items():
        salesperson_influence[salesperson_id] = len(customers_set)
    return salesperson_influence