import math

class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total_sum = 0
        
        max_so_far = -math.inf
        current_max = 0
        
        min_so_far = math.inf
        current_min = 0
        
        for x in nums:
            total_sum += x
            
            current_max = max(x, current_max + x)
            max_so_far = max(max_so_far, current_max)
            
            current_min = min(x, current_min + x)
            min_so_far = min(min_so_far, current_min)
            
        max_straight_sum = max_so_far
        max_wrap_sum = total_sum - min_so_far
        
        # If min_so_far == total_sum, it means the minimum sum subarray is the entire array itself.
        # This occurs when all numbers are negative (or all are zero).
        # In this specific case, max_wrap_sum would be 0 (total_sum - total_sum),
        # which is not a valid maximum sum if all numbers are negative.
        # The maximum sum must be the largest single element (or the max_straight_sum).
        if min_so_far == total_sum:
            return max_straight_sum
        else:
            return max(max_straight_sum, max_wrap_sum)