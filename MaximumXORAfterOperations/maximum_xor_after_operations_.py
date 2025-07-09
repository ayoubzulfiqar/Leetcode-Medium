class Solution:
    def maximumXOR(self, nums: list[int]) -> int:
        result_or = 0
        for num in nums:
            result_or |= num
        return result_or