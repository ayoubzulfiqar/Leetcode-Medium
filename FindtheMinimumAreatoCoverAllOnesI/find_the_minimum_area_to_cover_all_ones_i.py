class Solution:
    def minArea(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        min_row = rows
        max_row = -1
        min_col = cols
        max_col = -1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)
        
        height = max_row - min_row + 1
        width = max_col - min_col + 1

        return height * width