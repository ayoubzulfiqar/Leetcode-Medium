import bisect

class Solution:
    def minAbsoluteDifference(self, nums: list[int], x: int) -> int:
        n = len(nums)
        min_abs_diff = float('inf')
        
        candidates = [] 
        
        for i in range(n):
            if i >= x:
                bisect.insort_left(candidates, nums[i - x])
            
            if candidates:
                pos = bisect.bisect_left(candidates, nums[i])
                
                if pos < len(candidates):
                    min_abs_diff = min(min_abs_diff, abs(nums[i] - candidates[pos]))
                
                if pos > 0:
                    min_abs_diff = min(min_abs_diff, abs(nums[i] - candidates[pos - 1]))
                    
        return min_abs_diff