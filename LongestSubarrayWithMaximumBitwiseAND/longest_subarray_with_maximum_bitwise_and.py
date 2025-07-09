class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_val = max(nums)
        
        max_length = 0
        current_length = 0
        
        for num in nums:
            if num == max_val:
                current_length += 1
            else:
                current_length = 0
            
            if current_length > max_length:
                max_length = current_length
                
        return max_length