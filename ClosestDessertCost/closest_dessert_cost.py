class Solution:
    def closestCost(self, baseCosts: list[int], toppingCosts: list[int], target: int) -> int:
        topping_sums = {0}

        for cost in toppingCosts:
            new_sums = set()
            for s in topping_sums:
                new_sums.add(s)
                new_sums.add(s + cost)
                new_sums.add(s + 2 * cost)
            topping_sums = new_sums
        
        min_diff = float('inf')
        closest_cost = float('inf')

        for base_cost in baseCosts:
            for topping_sum in topping_sums:
                current_cost = base_cost + topping_sum
                current_diff = abs(current_cost - target)

                if current_diff < min_diff:
                    min_diff = current_diff
                    closest_cost = current_cost
                elif current_diff == min_diff:
                    if current_cost < closest_cost:
                        closest_cost = current_cost
        
        return closest_cost