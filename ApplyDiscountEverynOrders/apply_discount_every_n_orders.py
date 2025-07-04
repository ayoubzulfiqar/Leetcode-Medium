class Cashier:
    def __init__(self, n: int, discount: int, products: list[int], prices: list[int]):
        self.n = n
        self.discount_multiplier = (100 - discount) / 100.0
        self.product_prices = {}
        for i in range(len(products)):
            self.product_prices[products[i]] = prices[i]
        self.customer_count = 0

    def getBill(self, product: list[int], amount: list[int]) -> float:
        self.customer_count += 1
        
        subtotal = 0.0
        for i in range(len(product)):
            prod_id = product[i]
            qty = amount[i]
            subtotal += self.product_prices[prod_id] * qty
            
        if self.customer_count % self.n == 0:
            return subtotal * self.discount_multiplier
        else:
            return subtotal