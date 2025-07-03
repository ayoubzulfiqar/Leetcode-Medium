class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        n = len(values)
        
        dp = [[0] * n for _ in range(n)]
        
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                
                dp[i][j] = float('inf')
                
                for k in range(i + 1, j):
                    current_triangle_cost = values[i] * values[k] * values[j]
                    
                    total_cost = current_triangle_cost + dp[i][k] + dp[k][j]
                    
                    dp[i][j] = min(dp[i][j], total_cost)
                    
        return dp[0][n-1]