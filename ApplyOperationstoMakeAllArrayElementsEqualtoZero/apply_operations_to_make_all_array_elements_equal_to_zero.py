class Solution:
    def checkArray(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        diff = [0] * n
        
        current_active_reduction = 0
        
        for i in range(n):
            if i >= k:
                current_active_reduction -= diff[i - k]
            
            effective_val = nums[i] - current_active_reduction
            
            if effective_val < 0:
                return False
            
            if effective_val > 0:
                if i + k > n:
                    return False
                
                diff[i] = effective_val
                current_active_reduction += diff[i]
            
        return True