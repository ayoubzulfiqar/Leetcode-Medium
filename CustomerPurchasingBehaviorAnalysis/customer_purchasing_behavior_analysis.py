import collections

sample_data = [
    {"customer_id": "C001", "product": "Laptop", "category": "Electronics", "price": 1200, "date": "2023-01-15", "payment_method": "Credit Card"},
    {"customer_id": "C002", "product": "Mouse", "category": "Electronics", "price": 25, "date": "2023-01-15", "payment_method": "Debit Card"},
    {"customer_id": "C001", "product": "Keyboard", "category": "Electronics", "price": 75, "date": "2023-01-16", "payment_method": "Credit Card"},
    {"customer_id": "C003", "product": "T-Shirt", "category": "Apparel", "price": 30, "date": "2023-01-16", "payment_method": "PayPal"},
    {"customer_id": "C002", "product": "Monitor", "category": "Electronics", "price": 300, "date": "2023-01-17", "payment_method": "Credit Card"},
    {"customer_id": "C004", "product": "Book", "category": "Books", "price": 15, "date": "2023-01-17", "payment_method": "Debit Card"},
    {"customer_id": "C001", "product": "Webcam", "category": "Electronics", "price": 50, "date": "2023-01-18", "payment_method": "Credit Card"},
    {"customer_id": "C003", "product": "Jeans", "category": "Apparel", "price": 60, "date": "2023-01-18", "payment_method": "PayPal"},
    {"customer_id": "C005", "product": "Coffee Maker", "category": "Home Goods", "price": 100, "date": "2023-01-19", "payment_method": "Credit Card"},
    {"customer_id": "C002", "product": "Headphones", "category": "Electronics", "price": 150, "date": "2023-01-19", "payment_method": "Credit Card"},
    {"customer_id": "C001", "product": "Mouse Pad", "category": "Electronics", "price": 10, "date": "2023-01-20", "payment_method": "Credit Card"},
]

def analyze_total_sales_and_avg_transaction(data):
    total_sales = sum(item['price'] for item in data)
    num_transactions = len(data)
    avg_transaction_value = total_sales / num_transactions if num_transactions > 0 else 0
    return total_sales, num_transactions, avg_transaction_value

def analyze_popular_items(data):
    product_counts = collections.Counter(item['product'] for item in data)
    category_counts = collections.Counter(item['category'] for item in data)
    return product_counts, category_counts

def analyze_top_customers(data):
    customer_spending = collections.defaultdict(float)
    for item in data:
        customer_spending[item['customer_id']] += item['price']
    
    sorted_customers = sorted(customer_spending.items(), key=lambda x: x[1], reverse=True)
    return sorted_customers

def analyze_payment_methods(data):
    payment_method_counts = collections.Counter(item['payment_method'] for item in data)
    return payment_method_counts

def analyze_sales_by_month(data):
    sales_by_month = collections.defaultdict(float)
    for item in data:
        month_year = item['date'][:7]
        sales_by_month[month_year] += item['price']
    
    sorted_sales_by_month = sorted(sales_by_month.items())
    return sorted_sales_by_month

if __name__ == "__main__":
    
    total_sales, num_transactions, avg_transaction_value = analyze_total_sales_and_avg_transaction(sample_data)
    print("--- Overall Sales Metrics ---")
    print(f"Total Sales: ${total_sales:.2f}")
    print(f"Number of Transactions: {num_transactions}")
    print(f"Average Transaction Value: ${avg_transaction_value:.2f}\n")

    product_counts, category_counts = analyze_popular_items(sample_data)
    print("--- Popular Products ---")
    for product, count in product_counts.most_common(5):
        print(f"  {product}: {count} purchases")
    print("\n--- Popular Categories ---")
    for category, count in category_counts.most_common(5):
        print(f"  {category}: {count} purchases")
    print()

    top_customers = analyze_top_customers(sample_data)
    print("--- Top Customers by Spending ---")
    for customer_id, spent in top_customers:
        print(f"  {customer_id}: ${spent:.2f}")
    print()

    payment_methods = analyze_payment_methods(sample_data)
    print("--- Payment Method Distribution ---")
    for method, count in payment_methods.items():
        print(f"  {method}: {count} transactions")
    print()

    sales_by_month = analyze_sales_by_month(sample_data)
    print("--- Sales by Month ---")
    for month_year, sales in sales_by_month:
        print(f"  {month_year}: ${sales:.2f}")
    print()