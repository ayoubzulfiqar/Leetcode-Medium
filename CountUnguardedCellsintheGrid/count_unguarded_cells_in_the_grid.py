class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        EMPTY = 0
        GUARD = 1
        WALL = 2
        GUARDED = 3

        grid = [[EMPTY for _ in range(n)] for _ in range(m)]

        for r, c in guards:
            grid[r][c] = GUARD
        for r, c in walls:
            grid[r][c] = WALL

        for r_guard, c_guard in guards:
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 

            for dr, dc in directions:
                curr_r, curr_c = r_guard + dr, c_guard + dc
                while 0 <= curr_r < m and 0 <= curr_c < n:
                    cell_type = grid[curr_r][curr_c]
                    if cell_type == WALL or cell_type == GUARD:
                        break
                    elif cell_type == EMPTY:
                        grid[curr_r][curr_c] = GUARDED
                    
                    curr_r += dr
                    curr_c += dc
        
        unguarded_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == EMPTY:
                    unguarded_count += 1
        
        return unguarded_count