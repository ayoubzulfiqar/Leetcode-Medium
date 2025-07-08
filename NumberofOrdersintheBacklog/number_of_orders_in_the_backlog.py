import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders: list[list[int]]) -> int:
        buy_orders = []  # Max-heap: stores (-price, amount) for buy orders
        sell_orders = [] # Min-heap: stores (price, amount) for sell orders
        MOD = 10**9 + 7

        for price, amount, order_type in orders:
            if order_type == 0:  # Buy order
                current_buy_amount = amount
                # Try to match with sell orders from the backlog
                # Match if sell_orders exist, current buy amount is positive, and the smallest sell price is less than or equal to current buy price
                while current_buy_amount > 0 and sell_orders and sell_orders[0][0] <= price:
                    sell_price, sell_amount = heapq.heappop(sell_orders)
                    
                    matched_amount = min(current_buy_amount, sell_amount)
                    current_buy_amount -= matched_amount
                    sell_amount -= matched_amount
                    
                    if sell_amount > 0:
                        heapq.heappush(sell_orders, (sell_price, sell_amount))
                
                # If there's remaining buy amount, add it to the buy backlog
                if current_buy_amount > 0:
                    heapq.heappush(buy_orders, (-price, current_buy_amount))

            else:  # Sell order (order_type == 1)
                current_sell_amount = amount
                # Try to match with buy orders from the backlog
                # Match if buy_orders exist, current sell amount is positive, and the largest buy price is greater than or equal to current sell price
                while current_sell_amount > 0 and buy_orders and -buy_orders[0][0] >= price:
                    buy_price_neg, buy_amount = heapq.heappop(buy_orders)
                    buy_price = -buy_price_neg # Convert negative price back to original positive price
                    
                    matched_amount = min(current_sell_amount, buy_amount)
                    current_sell_amount -= matched_amount
                    buy_amount -= matched_amount
                    
                    if buy_amount > 0:
                        heapq.heappush(buy_orders, (-buy_price, buy_amount))
                
                # If there's remaining sell amount, add it to the sell backlog
                if current_sell_amount > 0:
                    heapq.heappush(sell_orders, (price, current_sell_amount))
        
        total_backlog_amount = 0
        for _, amount in buy_orders:
            total_backlog_amount = (total_backlog_amount + amount) % MOD
        
        for _, amount in sell_orders:
            total_backlog_amount = (total_backlog_amount + amount) % MOD
            
        return total_backlog_amount