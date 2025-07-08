import collections

class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        m = len(isWater)
        n = len(isWater[0])

        height = [[-1] * n for _ in range(m)]
        queue = collections.deque()

        for r in range(m):
            for c in range(n):
                if isWater[r][c] == 1:
                    height[r][c] = 0
                    queue.append((r, c))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and height[nr][nc] == -1:
                    height[nr][nc] = height[r][c] + 1
                    queue.append((nr, nc))
        
        return height