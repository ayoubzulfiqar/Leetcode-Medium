import math

class Solution:
    def maxScore(self, nums: list[int], x: int) -> int:
        ms_even = -math.inf
        ms_odd = -math.inf
        
        if nums[0] % 2 == 0:
            ms_even = nums[0]
        else:
            ms_odd = nums[0]
            
        for i in range(1, len(nums)):
            num = nums[i]
            parity = num % 2
            
            temp_ms_even = ms_even
            temp_ms_odd = ms_odd
            
            if parity == 0:
                ms_even = max(temp_ms_even + num, temp_ms_odd + num - x)
                ms_odd = temp_ms_odd 
            else:
                ms_odd = max(temp_ms_odd + num, temp_ms_even + num - x)
                ms_even = temp_ms_even
                
        return max(ms_even, ms_odd)