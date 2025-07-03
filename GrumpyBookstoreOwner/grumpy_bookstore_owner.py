class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        n = len(customers)

        base_satisfied_customers = 0
        for i in range(n):
            if grumpy[i] == 0:
                base_satisfied_customers += customers[i]

        current_bonus_customers = 0
        max_bonus_customers = 0

        for i in range(minutes):
            if grumpy[i] == 1:
                current_bonus_customers += customers[i]
        
        max_bonus_customers = current_bonus_customers

        for i in range(minutes, n):
            if grumpy[i - minutes] == 1:
                current_bonus_customers -= customers[i - minutes]
            
            if grumpy[i] == 1:
                current_bonus_customers += customers[i]
            
            max_bonus_customers = max(max_bonus_customers, current_bonus_customers)
        
        return base_satisfied_customers + max_bonus_customers