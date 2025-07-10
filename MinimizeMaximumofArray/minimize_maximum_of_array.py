class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        current_sum = 0
        max_val = 0 

        for i in range(len(nums)):
            current_sum += nums[i]
            max_val = max(max_val, (current_sum + i) // (i + 1))
            
        return max_val