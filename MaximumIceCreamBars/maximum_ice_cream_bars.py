class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        max_cost = 0
        for cost in costs:
            if cost > max_cost:
                max_cost = cost
        
        counts = [0] * (max_cost + 1)
        
        for cost in costs:
            counts[cost] += 1
            
        bought_bars = 0
        
        for cost_value in range(1, max_cost + 1):
            if counts[cost_value] > 0:
                num_available_at_this_cost = counts[cost_value]
                
                for _ in range(num_available_at_this_cost):
                    if coins >= cost_value:
                        coins -= cost_value
                        bought_bars += 1
                    else:
                        return bought_bars
                        
        return bought_bars