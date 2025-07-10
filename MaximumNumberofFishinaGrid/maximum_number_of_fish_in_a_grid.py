class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        max_fish = 0

        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n and grid[r][c] > 0 and (r, c) not in visited):
                return 0

            visited.add((r, c))
            
            current_fish_sum = grid[r][c]

            current_fish_sum += dfs(r + 1, c)
            current_fish_sum += dfs(r - 1, c)
            current_fish_sum += dfs(r, c + 1)
            current_fish_sum += dfs(r, c - 1)

            return current_fish_sum

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and (r, c) not in visited:
                    component_fish = dfs(r, c)
                    max_fish = max(max_fish, component_fish)

        return max_fish