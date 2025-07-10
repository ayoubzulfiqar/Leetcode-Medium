class Solution:
    def matrixSum(self, nums: list[list[int]]) -> int:
        rows = len(nums)
        cols = len(nums[0]) 

        for r in range(rows):
            nums[r].sort()

        total_score = 0

        for c_idx in range(cols):
            current_max_among_removed = 0
            for r_idx in range(rows):
                current_max_among_removed = max(current_max_among_removed, nums[r_idx][cols - 1 - c_idx])
            
            total_score += current_max_among_removed
        
        return total_score