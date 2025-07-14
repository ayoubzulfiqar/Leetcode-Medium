class Solution:
    def countPaths(self, grid: list[list[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7

        dp = [[[0] * 16 for _ in range(n)] for _ in range(m)]

        dp[0][0][grid[0][0]] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                current_cell_value = grid[i][j]

                for prev_xor_sum in range(16):
                    current_xor_sum = prev_xor_sum ^ current_cell_value
                    
                    if i > 0:
                        dp[i][j][current_xor_sum] = (dp[i][j][current_xor_sum] + dp[i-1][j][prev_xor_sum]) % MOD
                    
                    if j > 0:
                        dp[i][j][current_xor_sum] = (dp[i][j][current_xor_sum] + dp[i][j-1][prev_xor_sum]) % MOD
        
        return dp[m-1][n-1][k]