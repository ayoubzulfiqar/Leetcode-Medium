class Solution:
    def maxStrength(self, nums: list[int]) -> int:
        n = len(nums)
        max_strength = float('-inf')

        for i in range(1, 1 << n):
            current_product = 1
            for j in range(n):
                if (i >> j) & 1:
                    current_product *= nums[j]
            max_strength = max(max_strength, current_product)
        
        return max_strength