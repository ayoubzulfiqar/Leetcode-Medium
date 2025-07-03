class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        n = len(arr)
        
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            current_max_val = 0
            
            for j in range(1, k + 1):
                start_index = i - j
                
                if start_index < 0:
                    break
                
                current_max_val = max(current_max_val, arr[start_index])
                
                dp[i] = max(dp[i], dp[start_index] + current_max_val * j)
        
        return dp[n]