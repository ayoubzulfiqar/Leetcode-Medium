class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        n = len(nums)
        
        indexed_nums = []
        for i in range(n):
            indexed_nums.append((nums[i], i))
        
        indexed_nums.sort()
        
        max_width = 0
        
        min_idx_so_far = indexed_nums[0][1]
        
        for k in range(1, n):
            current_idx = indexed_nums[k][1]
            
            max_width = max(max_width, current_idx - min_idx_so_far)
            
            min_idx_so_far = min(min_idx_so_far, current_idx)
                
        return max_width