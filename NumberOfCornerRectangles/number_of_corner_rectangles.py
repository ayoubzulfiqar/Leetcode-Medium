class Solution:
    def countCornerRectangles(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        if cols == 0:
            return 0

        count = 0

        for r1 in range(rows):
            for r2 in range(r1 + 1, rows):
                common_ones_in_columns = 0
                for c in range(cols):
                    if grid[r1][c] == 1 and grid[r2][c] == 1:
                        common_ones_in_columns += 1
                
                count += common_ones_in_columns * (common_ones_in_columns - 1) // 2
        
        return count