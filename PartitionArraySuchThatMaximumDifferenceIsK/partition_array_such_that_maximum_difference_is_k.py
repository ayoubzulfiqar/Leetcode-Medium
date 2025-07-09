class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        
        count = 1
        min_val_in_current_subsequence = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] - min_val_in_current_subsequence > k:
                count += 1
                min_val_in_current_subsequence = nums[i]
                
        return count