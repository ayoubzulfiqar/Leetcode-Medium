class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        dp_plus = 0
        dp_minus = float('-inf')

        for num in nums:
            new_dp_plus = max(dp_plus, dp_minus + num, num)
            new_dp_minus = max(dp_minus, dp_plus - num)
            
            dp_plus = new_dp_plus
            dp_minus = new_dp_minus
            
        return dp_plus