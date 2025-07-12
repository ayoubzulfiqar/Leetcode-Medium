class Solution:
    def minimumOperations(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        counts = [[0] * 10 for _ in range(n)]
        for j in range(n):
            for i in range(m):
                counts[j][grid[i][j]] += 1

        cost = [[0] * 10 for _ in range(n)]
        for j in range(n):
            for val in range(10):
                cost[j][val] = m - counts[j][val]

        prev_dp = [0] * 10
        curr_dp = [0] * 10

        for val in range(10):
            prev_dp[val] = cost[0][val]

        for j in range(1, n):
            min1 = float('inf')
            val1 = -1
            min2 = float('inf')

            for prev_val in range(10):
                if prev_dp[prev_val] < min1:
                    min2 = min1
                    min1 = prev_dp[prev_val]
                    val1 = prev_val
                elif prev_dp[prev_val] < min2:
                    min2 = prev_dp[prev_val]
            
            for val in range(10):
                if val != val1:
                    curr_dp[val] = cost[j][val] + min1
                else:
                    curr_dp[val] = cost[j][val] + min2
            
            prev_dp = curr_dp[:]

        return min(prev_dp)