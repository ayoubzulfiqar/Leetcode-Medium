from datetime import date

class Solution:
    def findPrices(self, products: list[list[int, int, str]]) -> list[list[int]]:
        target_date = date(2019, 8, 16)
        
        product_prices = {}
        
        for product_id, _, _ in products:
            product_prices[product_id] = 10 

        relevant_changes = []
        for product_id, new_price, change_date_str in products:
            change_date_obj = date.fromisoformat(change_date_str)
            if change_date_obj <= target_date:
                relevant_changes.append((product_id, new_price, change_date_obj))
        
        relevant_changes.sort(key=lambda x: (x[0], x[2]))

        for product_id, new_price, _ in relevant_changes:
            product_prices[product_id] = new_price
            
        result = [[pid, price] for pid, price in product_prices.items()]
        
        return result