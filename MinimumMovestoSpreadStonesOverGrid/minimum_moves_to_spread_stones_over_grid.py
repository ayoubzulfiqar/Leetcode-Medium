```python
import math

class Solution:
    def minMovesToSpreadStones(self, grid: list[list[int]]) -> int:
        sources = []
        targets = []

        for r in range(3):
            for c in range(3):
                if grid[r][c] > 1:
                    for _ in range(grid[r][c] - 1):
                        sources.append((r, c))
                elif grid[r][c] == 0:
                    targets.append((r, c))

        k = len(sources)
        min_total_moves = float('inf')

        def solve(source_idx, current_cost, used_targets_mask):
            nonlocal min_total_moves

            if current_cost >= min_total_moves:
                return

            if source_idx == k:
                min_total_moves = min(min_total_moves, current_cost)
                return

            for target_idx in range(k):
                if not (used_targets_mask & (1 << target_idx)):
                    s_r, s_c = sources[source_idx]
                    t_r, t_c = targets[target_idx]
                    dist = abs(s_r - t_r) + abs(s_c - t_c)
                    solve(source_idx + 1, current_cost + dist, used_targets_mask | (1 << target_idx))

        solve(0, 0, 0)
        return min_total_moves

```