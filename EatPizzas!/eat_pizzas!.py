class Solution:
    def eatPizzas(self, pizzas: list[int]) -> int:
        pizzas.sort()
        
        n = len(pizzas)
        total_weight_gained = 0
        
        left = 0
        right = n - 1
        day_count = 1
        
        while left < right:
            if day_count % 2 == 1: # Odd-numbered day (1-indexed)
                # To maximize Z, we pick the largest available pizza as Z.
                # We consume pizzas[right] (Z), and pizzas[left], pizzas[left+1], pizzas[left+2] (W, X, Y).
                total_weight_gained += pizzas[right]
                left += 3
                right -= 1
            else: # Even-numbered day
                # To maximize Y, we pick the second largest available pizza as Y.
                # We consume pizzas[right-1] (Y), pizzas[right] (Z), and pizzas[left], pizzas[left+1] (W, X).
                total_weight_gained += pizzas[right-1]
                left += 2
                right -= 2
            
            day_count += 1
            
        return total_weight_gained