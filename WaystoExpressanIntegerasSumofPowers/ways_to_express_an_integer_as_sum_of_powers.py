class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * (n + 1)
        
        dp[0] = 1
        
        current_base = 1
        while True:
            power_val = current_base ** x
            
            if power_val > n:
                break
            
            for j in range(n, power_val - 1, -1):
                dp[j] = (dp[j] + dp[j - power_val]) % MOD
            
            current_base += 1
            
        return dp[n]