class Solution:
    def minImpossibleOR(self, nums: list[int]) -> int:
        nums.sort()
        current_max_or_sum = 0
        for num in nums:
            if num > current_max_or_sum + 1:
                return current_max_or_sum + 1
            current_max_or_sum |= num
        return current_max_or_sum + 1