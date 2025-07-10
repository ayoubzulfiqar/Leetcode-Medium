class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        reachable_rows = set()
        for r in range(m):
            reachable_rows.add(r)
        
        max_moves = 0

        for col in range(n - 1):
            next_reachable_rows = set()
            moved_in_current_col = False

            for r in reachable_rows:
                current_val = grid[r][col]

                # Move to (row-1, col+1)
                if r - 1 >= 0 and grid[r - 1][col + 1] > current_val:
                    next_reachable_rows.add(r - 1)
                    moved_in_current_col = True
                
                # Move to (row, col+1)
                if grid[r][col + 1] > current_val:
                    next_reachable_rows.add(r)
                    moved_in_current_col = True
                
                # Move to (row+1, col+1)
                if r + 1 < m and grid[r + 1][col + 1] > current_val:
                    next_reachable_rows.add(r + 1)
                    moved_in_current_col = True
            
            if not moved_in_current_col:
                break
            
            reachable_rows = next_reachable_rows
            max_moves += 1
        
        return max_moves