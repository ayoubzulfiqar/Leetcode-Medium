class Solution:
    def max_ribbon_pieces(self, n: int, ribbonLengths: list[int]) -> int:
        dp = [-1] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for length in ribbonLengths:
                if i >= length:
                    if dp[i - length] != -1:
                        dp[i] = max(dp[i], dp[i - length] + 1)
        
        return dp[n]