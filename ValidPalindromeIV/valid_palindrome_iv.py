class Solution:
    def isValidPalindromeIV(self, s: str, k: int) -> bool:
        n = len(s)
        if n == 0:
            return True
        
        dp = [[0] * n for _ in range(n)]

        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] if L > 2 else 0
                else:
                    dp[i][j] = (dp[i+1][j-1] if L > 2 else 0) + 1
        
        return dp[0][n-1] <= k