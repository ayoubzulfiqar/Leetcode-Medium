class Solution:
    def isIdealPermutation(self, nums: list[int]) -> bool:
        n = len(nums)

        if n < 3:
            return True

        min_suffix = [0] * n
        min_suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(nums[i], min_suffix[i + 1])

        for i in range(n - 2):
            if nums[i] > min_suffix[i + 2]:
                return False

        return True