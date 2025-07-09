class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        
        valid_splits_count = 0
        current_prefix_sum = 0
        
        for i in range(n - 1): 
            current_prefix_sum += nums[i]
            
            current_suffix_sum = total_sum - current_prefix_sum
            
            if current_prefix_sum >= current_suffix_sum:
                valid_splits_count += 1
                
        return valid_splits_count