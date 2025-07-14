import math

def maxSubarraySumDivisibleByK(nums: list[int], k: int) -> int:
    max_subarray_sum = -math.inf
    
    min_prefix_sums_by_remainder = [math.inf] * k
    
    min_prefix_sums_by_remainder[0] = 0
    
    current_prefix_sum = 0
    
    for i in range(len(nums)):
        current_prefix_sum += nums[i]
        
        idx_for_remainder = i + 1
        remainder = idx_for_remainder % k
        
        if min_prefix_sums_by_remainder[remainder] != math.inf:
            max_subarray_sum = max(max_subarray_sum, current_prefix_sum - min_prefix_sums_by_remainder[remainder])
        
        min_prefix_sums_by_remainder[remainder] = min(min_prefix_sums_by_remainder[remainder], current_prefix_sum)
            
    return max_subarray_sum