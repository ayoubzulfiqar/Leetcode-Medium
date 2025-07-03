class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_overall_gold = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r: int, c: int) -> int:
            if not (0 <= r < m and 0 <= c < n) or grid[r][c] == 0:
                return 0

            current_gold = grid[r][c]
            grid[r][c] = 0  # Mark as visited for the current path

            max_gold_from_neighbors = 0
            for dr, dc in directions:
                next_r, next_c = r + dr, c + dc
                max_gold_from_neighbors = max(max_gold_from_neighbors, dfs(next_r, next_c))

            grid[r][c] = current_gold  # Backtrack: restore gold for other paths

            return current_gold + max_gold_from_neighbors

        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0:
                    max_overall_gold = max(max_overall_gold, dfs(r, c))

        return max_overall_gold