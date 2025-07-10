```python
import math

class Solution:
    def minLinesToCoverPoints(self, points: list[list[int]]) -> int:
        n = len(points)

        if n == 0:
            return 0
        if n <= 2:
            return 1

        line_masks = set()

        for i in range(n):
            line_masks.add(1 << i)

        for i in range(n):
            for j in range(i + 1, n):
                mask = (1 << i) | (1 << j)
                p1 = points[i]
                p2 = points[j]

                for k in range(n):
                    if k == i or k == j:
                        continue
                    p3 = points[k]

                    if (p2[1] - p1[1]) * (p3[0] - p2[0]) == (p3[1] - p2[1]) * (p2[0] - p1[0]):
                        mask |= (1 << k)
                line_masks.add(mask)

        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1, 1 << n):
            first_uncovered_point_idx = 0
            while not ((mask >> first_uncovered_point_idx) & 1):
                first_uncovered_point_idx += 1

            for line_mask in line_masks:
                if (line_mask >> first_uncovered_point_idx) & 1:
                    dp[mask] = min(dp[mask], 1 + dp[mask & (~line_mask)])

        return dp[(1 << n) - 1]

```