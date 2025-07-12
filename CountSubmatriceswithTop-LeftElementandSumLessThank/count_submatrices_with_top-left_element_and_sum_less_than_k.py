class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        count = 0

        for r in range(m):
            for c in range(n):
                current_sum = grid[r][c]
                
                if r > 0:
                    current_sum += dp[r-1][c]
                
                if c > 0:
                    current_sum += dp[r][c-1]
                
                if r > 0 and c > 0:
                    current_sum -= dp[r-1][c-1]
                
                dp[r][c] = current_sum
                
                if dp[r][c] <= k:
                    count += 1
                    
        return count