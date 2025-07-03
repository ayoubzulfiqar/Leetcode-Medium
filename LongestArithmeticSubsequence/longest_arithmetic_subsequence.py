class Solution:
    def longestArithmeticSubsequence(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        dp = [{} for _ in range(n)]
        
        max_len = 2 

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                length_ending_at_j = dp[j].get(diff, 1) 
                
                dp[i][diff] = length_ending_at_j + 1
                
                max_len = max(max_len, dp[i][diff])
                
        return max_len