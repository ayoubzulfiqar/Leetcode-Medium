class Solution:
    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row_prefix = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                row_prefix[i][j+1] = row_prefix[i][j] + grid[i][j]

        col_prefix = [[0] * n for _ in range(m + 1)]
        for j in range(n):
            for i in range(m):
                col_prefix[i+1][j] = col_prefix[i][j] + grid[i][j]

        diag1_prefix = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diag1_prefix[i][j] = grid[i][j]
                if i > 0 and j > 0:
                    diag1_prefix[i][j] += diag1_prefix[i-1][j-1]

        diag2_prefix =