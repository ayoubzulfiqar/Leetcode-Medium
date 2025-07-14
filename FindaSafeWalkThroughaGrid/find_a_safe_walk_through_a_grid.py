import collections

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])

        max_health_at_cell = [[-1] * n for _ in range(m)]

        initial_health_after_start = health - grid[0][0]

        if initial_health_after_start <= 0:
            return False

        q = collections.deque()

        q.append((0, 0, initial_health_after_start))
        max_health_at_cell[0][0] = initial_health_after_start

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            r, c, current_health = q.popleft()

            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_health = current_health - grid[nr][nc]

                    if new_health >= 1 and new_health > max_health_at_cell[nr][nc]:
                        max_health_at_cell[nr][nc] = new_health
                        q.append((nr, nc, new_health))

        return False