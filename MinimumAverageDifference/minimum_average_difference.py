class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        
        min_avg_diff = float('inf')
        result_index = -1
        
        current_prefix_sum = 0
        
        for i in range(n):
            current_prefix_sum += nums[i]
            
            # Calculate prefix average
            prefix_avg = current_prefix_sum // (i + 1)
            
            # Calculate suffix average
            suffix_sum = total_sum - current_prefix_sum
            suffix_count = n - i - 1
            
            if suffix_count == 0:
                suffix_avg = 0
            else:
                suffix_avg = suffix_sum // suffix_count
            
            # Calculate current average difference
            current_diff = abs(prefix_avg - suffix_avg)
            
            # Update minimum average difference and result index
            if current_diff < min_avg_diff:
                min_avg_diff = current_diff
                result_index = i
        
        return result_index