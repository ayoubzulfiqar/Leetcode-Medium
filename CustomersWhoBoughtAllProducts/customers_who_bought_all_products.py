class Solution:
    def customers_who_bought_all_products(self, customer_table: list[list[int]], product_table: list[list[int]]) -> list[int]:
        # Step 1: Get all unique product keys from the Product table.
        # This represents the complete set of products available.
        all_products_set = {p[0] for p in product_table}
        
        # Step 2: Group purchases by customer.
        # Create a dictionary where keys are customer_ids and values are sets
        # of product_keys bought by that customer.
        customer_purchases = {}
        for customer_id, product_key in customer_table:
            if customer_id not in customer_purchases:
                customer_purchases[customer_id] = set()
            customer_purchases[customer_id].add(product_key)
            
        # Step 3: Identify customers who bought all products.
        # Iterate through the grouped customer purchases and compare each customer's
        # set of bought products with the set of all available products.
        result_customer_ids = []
        for customer_id, products_bought_set in customer_purchases.items():
            # If the set of products bought by the customer is exactly equal to
            # the set of all products, then this customer bought all products.
            if products_bought_set == all_products_set:
                result_customer_ids.append(customer_id)
                
        return result_customer_ids