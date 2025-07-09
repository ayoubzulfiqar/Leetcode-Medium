class Solution:
    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        val_to_idx = {}
        for i, num in enumerate(nums):
            val_to_idx[num] = i
        
        for old_val, new_val in operations:
            idx = val_to_idx[old_val]
            nums[idx] = new_val
            del val_to_idx[old_val]
            val_to_idx[new_val] = idx
            
        return nums