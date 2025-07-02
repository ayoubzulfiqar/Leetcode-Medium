class Solution:
    def maxA(self, N: int) -> int:
        if N <= 6:
            return N

        dp = [0] * (N + 1)

        for i in range(1, 7):
            dp[i] = i

        for i in range(7, N + 1):
            dp[i] = dp[i-1] + 1
            for j in range(1, i - 2):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
        
        return dp[N]