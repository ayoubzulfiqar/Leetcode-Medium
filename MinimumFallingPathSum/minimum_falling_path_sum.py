class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        
        dp = [[0] * n for _ in range(n)]
        
        for j in range(n):
            dp[0][j] = matrix[0][j]
            
        for i in range(1, n):
            for j in range(n):
                min_prev_sum = float('inf')
                
                if j - 1 >= 0:
                    min_prev_sum = min(min_prev_sum, dp[i-1][j-1])
                
                min_prev_sum = min(min_prev_sum, dp[i-1][j])
                
                if j + 1 < n:
                    min_prev_sum = min(min_prev_sum, dp[i-1][j+1])
                
                dp[i][j] = matrix[i][j] + min_prev_sum
        
        return min(dp[n-1])