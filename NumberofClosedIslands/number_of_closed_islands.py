class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def iterative_dfs(r_start, c_start):
            stack = [(r_start, c_start)]
            grid[r_start][c_start] = 1

            while stack:
                r, c = stack.pop()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        stack.append((nr, nc))

        for c in range(n):
            if grid[0][c] == 0:
                iterative_dfs(0, c)
            if grid[m - 1][c] == 0:
                iterative_dfs(m - 1, c)
        
        for r in range(1, m - 1):
            if grid[r][0] == 0:
                iterative_dfs(r, 0)
            if grid[r][n - 1] == 0:
                iterative_dfs(r, n - 1)

        closed_islands_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    closed_islands_count += 1
                    iterative_dfs(r, c)

        return closed_islands_count