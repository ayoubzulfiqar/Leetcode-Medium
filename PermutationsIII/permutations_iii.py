class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []
        path = []
        nums.sort()
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                result.append(list(path))
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                path.append(nums[i])
                used[i] = True
                backtrack()
                used[i] = False
                path.pop()

        backtrack()
        return result