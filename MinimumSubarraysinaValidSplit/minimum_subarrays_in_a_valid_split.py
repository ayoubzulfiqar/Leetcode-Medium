class Solution:
    def minSubarrays(self, nums: list[int]) -> int:
        if not nums:
            return 0

        num_subarrays = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                num_subarrays += 1
        return num_subarrays