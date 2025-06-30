class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_so_far = nums[0]
        current_max = nums[0]
        current_min = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            
            # Store the current_max from the previous iteration
            # as it's needed for calculating both new current_max and new current_min
            temp_current_max = current_max 
            
            current_max = max(num, num * temp_current_max, num * current_min)
            current_min = min(num, num * temp_current_max, num * current_min)
            
            max_so_far = max(max_so_far, current_max)
            
        return max_so_far