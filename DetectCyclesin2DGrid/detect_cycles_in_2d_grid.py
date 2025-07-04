class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, pr, pc, char_val):
            visited[r][c] = True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == char_val:
                    if (nr, nc) == (pr, pc):
                        continue
                    
                    if visited[nr][nc]:
                        return True
                    
                    if dfs(nr, nc, r, c, char_val):
                        return True
            return False

        for r in range(m):
            for c in range(n):
                if not visited[r][c]:
                    if dfs(r, c, -1, -1, grid[r][c]):
                        return True
        
        return False