class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7

        dp_max = [[0] * n for _ in range(m)]
        dp_min = [[0] * n for _ in range(m)]

        dp_max[0][0] = grid[0][0]
        dp_min[0][0] = grid[0][0]

        for j in range(1, n):
            val = grid[0][j]
            if val >= 0:
                dp_max[0][j] = dp_max[0][j-1] * val
                dp_min[0][j] = dp_min[0][j-1] * val
            else:
                dp_max[0][j] = dp_min[0][j-1] * val
                dp_min[0][j] = dp_max[0][j-1] * val

        for i in range(1, m):
            val = grid[i][0]
            if val >= 0:
                dp_max[i][0] = dp_max[i-1][0] * val
                dp_min[i][0] = dp_min[i-1][0] * val
            else:
                dp_max[i][0] = dp_min[i-1][0] * val
                dp_min[i][0] = dp_max[i-1][0] * val

        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]

                from_top_max = dp_max[i-1][j] * val
                from_top_min = dp_min[i-1][j] * val
                from_left_max = dp_max[i][j-1] * val
                from_left_min = dp_min[i][j-1] * val

                if val >= 0:
                    dp_max[i][j] = max(from_top_max, from_left_max)
                    dp_min[i][j] = min(from_top_min, from_left_min)
                else:
                    dp_max[i][j] = max(from_top_min, from_left_min)
                    dp_min[i][j] = min(from_top_max, from_left_max)

        result = dp_max[m-1][n-1]

        if result < 0:
            return -1
        else:
            return result % MOD