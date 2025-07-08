class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: list[int]) -> int:
        n = len(nextVisit)
        MOD = 10**9 + 7

        dp = [0] * n
        
        for i in range(1, n):
            dp[i] = (2 * dp[i-1] - dp[nextVisit[i-1]] + 2 + MOD) % MOD
            
        return dp[n-1]