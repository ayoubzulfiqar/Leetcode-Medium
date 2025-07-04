import collections

class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        connections = {
            1: {(0, -1), (0, 1)},
            2: {(-1, 0), (1, 0)},
            3: {(0, -1), (1, 0)},
            4: {(0, 1), (1, 0)},
            5: {(0, -1), (-1, 0)},
            6: {(0, 1), (-1, 0)}
        }

        q = collections.deque([(0, 0)])
        visited = set([(0, 0)])

        while q:
            r, c = q.popleft()

            if r == m - 1 and c == n - 1:
                return True

            current_street_type = grid[r][c]

            for dr, dc in connections[current_street_type]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    if (nr, nc) not in visited:
                        reverse_dr, reverse_dc = -dr, -dc
                        if (reverse_dr, reverse_dc) in connections[grid[nr][nc]]:
                            visited.add((nr, nc))
                            q.append((nr, nc))
        
        return False