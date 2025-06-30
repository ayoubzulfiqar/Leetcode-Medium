class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        n = len(nums)
        used = [False] * n

        def backtrack(current_permutation):
            if len(current_permutation) == n:
                result.append(list(current_permutation))
                return

            for i in range(n):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                current_permutation.append(nums[i])
                used[i] = True
                backtrack(current_permutation)
                used[i] = False
                current_permutation.pop()

        backtrack([])
        return result