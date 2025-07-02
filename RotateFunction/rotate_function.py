class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        
        total_sum = sum(nums)
        
        current_F = 0
        for i in range(n):
            current_F += i * nums[i]
            
        max_F = current_F
        
        for k in range(n - 1):
            # current_F holds F(k) for the current iteration
            # We want to calculate F(k+1) using the recurrence:
            # F(k+1) = F(k) + total_sum - n * arr_k[n-1]
            # The element arr_k[n-1] is the element that was at the last position
            # of the array rotated k times. This corresponds to nums[n - 1 - k]
            # in the original unrotated array.
            
            element_at_last_position_of_arr_k = nums[n - 1 - k]
            
            current_F = current_F + total_sum - n * element_at_last_position_of_arr_k
            max_F = max(max_F, current_F)
            
        return max_F