```python
import sys

sys.setrecursionlimit(2 * 10**5)

class Solution:
    def solve(self, n: int, edges: list[tuple[int, int, int]]) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 0

        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        dp = [[0, -float('inf')] for _ in range(n)]

        def dfs(u: int, parent: int):
            sum_max_child_scores = 0

            for v, weight in adj[u]:
                if v == parent:
                    continue

                dfs(v, u)

                sum_max_child_scores += max(dp[v][0], dp[v][1])

            dp[u][0] = sum_max_child_scores

            for v, weight in adj[u]:
                if v == parent:
                    continue
                
                current_match_score = weight + dp[v][0] + \
                                      (sum_max_child_scores - max(dp[v][0], dp[v][1]))
                
                dp[u][1] = max(dp[u][1], current_match_score)

        dfs(0, -1)

        return max(dp[0][0], dp[0][1])

```