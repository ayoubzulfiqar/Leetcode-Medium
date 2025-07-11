class Solution:
    def minCost(self, nums: list[int], x: int) -> int:
        n = len(nums)
        
        min_costs_per_type = list(nums)
        
        overall_min_total_cost = sum(min_costs_per_type)
        
        for k in range(1, n):
            cost_of_operations = k * x
            
            for j in range(n):
                min_costs_per_type[(j + k) % n] = min(min_costs_per_type[(j + k) % n], nums[j])
            
            current_rotation_total_cost = cost_of_operations + sum(min_costs_per_type)
            
            overall_min_total_cost = min(overall_min_total_cost, current_rotation_total_cost)
            
        return overall_min_total_cost