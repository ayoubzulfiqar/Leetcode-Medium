import collections

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific_reachable = [[False] * n for _ in range(m)]
        atlantic_reachable = [[False] * n for _ in range(m)]

        q_pacific = collections.deque()
        q_atlantic = collections.deque()

        for r in range(m):
            q_pacific.append((r, 0))
            pacific_reachable[r][0] = True
        for c in range(1, n):
            q_pacific.append((0, c))
            pacific_reachable[0][c] = True

        for r in range(m):
            q_atlantic.append((r, n - 1))
            atlantic_reachable[r][n - 1] = True
        for c in range(n - 1):
            q_atlantic.append((m - 1, c))
            atlantic_reachable[m - 1][c] = True

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(q, reachable_grid):
            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and not reachable_grid[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        reachable_grid[nr][nc] = True
                        q.append((nr, nc))

        bfs(q_pacific, pacific_reachable)
        bfs(q_atlantic, atlantic_reachable)

        result = []
        for r in range(m):
            for c in range(n):
                if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                    result.append([r, c])

        return result