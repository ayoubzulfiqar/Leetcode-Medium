class Solution:
    def minOperationsMaxProfit(self, customers: list[int], boardingCost: int, runningCost: int) -> int:
        max_profit = -1
        min_rotations_for_max_profit = -1
        
        current_profit = 0
        total_boarded_customers = 0
        waiting_customers = 0
        rotations = 0
        
        n = len(customers)
        customer_idx = 0
        
        while customer_idx < n or waiting_customers > 0:
            rotations += 1
            
            if customer_idx < n:
                waiting_customers += customers[customer_idx]
                customer_idx += 1
            
            boarded_this_turn = min(waiting_customers, 4)
            waiting_customers -= boarded_this_turn
            total_boarded_customers += boarded_this_turn
            
            current_profit = total_boarded_customers * boardingCost - rotations * runningCost
            
            if current_profit > max_profit:
                max_profit = current_profit
                min_rotations_for_max_profit = rotations
            
        return min_rotations_for_max_profit