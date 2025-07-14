import math

class Solution:
    def minTime(self, strength: list[int], k: int) -> int:
        n = len(strength)
        
        dp = [float('inf')] * (1 << n)
        
        dp[0] = 0
        
        for mask in range(1, 1 << n):
            for i in range(n):
                if (mask >> i) & 1:
                    prev_mask = mask ^ (1 << i)
                    
                    if dp[prev_mask] == float('inf'):
                        continue
                    
                    num_broken_before_i = bin(prev_mask).count('1')
                    
                    current_x = 1 + num_broken_before_i * k
                    
                    time_for_current_lock = math.ceil(strength[i] / current_x)
                    
                    dp[mask] = min(dp[mask], dp[prev_mask] + time_for_current_lock)
                    
        return dp[(1 << n) - 1]