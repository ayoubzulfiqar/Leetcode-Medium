class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0 

        max_so_far = nums[0]
        current_max = nums[0]

        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            max_so_far = max(max_so_far, current_max)
        
        return max_so_far