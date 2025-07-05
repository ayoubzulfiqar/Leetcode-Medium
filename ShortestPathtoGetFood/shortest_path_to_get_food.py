import collections

class Solution:
    def getFood(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        start_r, start_c = -1, -1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'S':
                    start_r, start_c = r, c
                    break
            if start_r != -1:
                break

        queue = collections.deque([(start_r, start_c, 0)])
        visited = {(start_r, start_c)}

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Right, Left, Down, Up

        while queue:
            r, c, dist = queue.popleft()

            if grid[r][c] == '#':
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] != 'X' and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc, dist + 1))

        return -1