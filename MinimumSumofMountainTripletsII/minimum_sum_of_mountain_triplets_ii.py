import math

class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        n = len(nums)
        
        min_prefix = [math.inf] * n
        for i in range(1, n):
            min_prefix[i] = min(min_prefix[i-1], nums[i-1])
            
        min_suffix = [math.inf] * n
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(min_suffix[i+1], nums[i+1])
            
        min_total_sum = math.inf
        
        for j in range(1, n - 1):
            left_val = min_prefix[j]
            right_val = min_suffix[j]
            
            if left_val < nums[j] and right_val < nums[j]:
                current_sum = left_val + nums[j] + right_val
                min_total_sum = min(min_total_sum, current_sum)
                
        if min_total_sum == math.inf:
            return -1
        else:
            return min_total_sum