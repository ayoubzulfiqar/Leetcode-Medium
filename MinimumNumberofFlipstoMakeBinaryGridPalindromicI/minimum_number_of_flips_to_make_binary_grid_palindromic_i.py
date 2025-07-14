class Solution:
    def minimumFlips(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        total_row_flips = 0
        for r in range(m):
            for c in range(n // 2):
                if grid[r][c] != grid[r][n - 1 - c]:
                    total_row_flips += 1

        total_col_flips = 0
        for c in range(n):
            for r in range(m // 2):
                if grid[r][c] != grid[m - 1 - r][c]:
                    total_col_flips += 1

        return min(total_row_flips, total_col_flips)