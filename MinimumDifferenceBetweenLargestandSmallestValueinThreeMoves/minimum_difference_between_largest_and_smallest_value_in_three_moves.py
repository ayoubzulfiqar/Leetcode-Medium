class Solution:
    def minDifference(self, nums: list[int]) -> int:
        n = len(nums)

        if n <= 4:
            return 0

        nums.sort()

        diff1 = nums[n - 4] - nums[0]
        diff2 = nums[n - 3] - nums[1]
        diff3 = nums[n - 2] - nums[2]
        diff4 = nums[n - 1] - nums[3]

        return min(diff1, diff2, diff3, diff4)