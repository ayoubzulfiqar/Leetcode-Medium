class Solution:
    def numberOfCleanedRooms(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        r, c = 0, 0
        d_idx = 0

        cleaned_cells = set()
        visited_states = set()

        while True:
            cleaned_cells.add((r, c))

            if (r, c, d_idx) in visited_states:
                break
            
            visited_states.add((r, c, d_idx))

            nr, nc = r + dr[d_idx], c + dc[d_idx]

            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                r, c = nr, nc
            else:
                d_idx = (d_idx + 1) % 4
        
        return len(cleaned_cells)