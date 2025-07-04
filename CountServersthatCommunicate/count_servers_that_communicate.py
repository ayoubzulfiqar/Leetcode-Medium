class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row_counts = [0] * m
        col_counts = [0] * n

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1

        communicating_servers_count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if row_counts[r] > 1 or col_counts[c] > 1:
                        communicating_servers_count += 1
        
        return communicating_servers_count