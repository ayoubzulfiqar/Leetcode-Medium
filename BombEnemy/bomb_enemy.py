class Solution:
    def maxKilledEnemies(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        
        max_enemies = 0
        
        col_hits = [0] * cols 
        
        for r in range(rows):
            row_hits = 0
            
            for c in range(cols):
                # Calculate row_hits for the current segment
                # If it's the beginning of a row or we just passed a wall, recalculate row_hits
                if c == 0 or grid[r][c-1] == 'W':
                    row_hits = 0
                    for k in range(c, cols):
                        if grid[r][k] == 'W':
                            break
                        if grid[r][k] == 'E':
                            row_hits += 1
                
                # Calculate col_hits[c] for the current segment
                # If it's the beginning of a column or we just passed a wall in this column, recalculate col_hits[c]
                if r == 0 or grid[r-1][c] == 'W':
                    col_hits[c] = 0
                    for k in range(r, rows):
                        if grid[k][c] == 'W':
                            break
                        if grid[k][c] == 'E':
                            col_hits[c] += 1
                
                # If the current cell is an empty cell, it's a potential bomb placement
                if grid[r][c] == '0':
                    max_enemies = max(max_enemies, row_hits + col_hits[c])
                    
        return max_enemies