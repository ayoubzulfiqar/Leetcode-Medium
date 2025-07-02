class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        max_row_heights = [0] * n
        for r in range(n):
            max_row_heights[r] = max(grid[r])
            
        max_col_heights = [0] * n
        for c in range(n):
            current_col_max = 0
            for r in range(n):
                if grid[r][c] > current_col_max:
                    current_col_max = grid[r][c]
            max_col_heights[c] = current_col_max
            
        total_increase = 0
        
        for r in range(n):
            for c in range(n):
                allowed_max_height = min(max_row_heights[r], max_col_heights[c])
                total_increase += (allowed_max_height - grid[r][c])
                
        return total_increase