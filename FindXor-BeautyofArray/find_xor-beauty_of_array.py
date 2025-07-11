class Solution:
    def xorBeauty(self, nums: list[int]) -> int:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        return xor_sum