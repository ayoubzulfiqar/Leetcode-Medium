```python
import collections
import heapq

class Solution:
    def countRestrictedPaths(self, n: int, edges: list[list[int]]) -> int:
        MOD = 10**9 + 7

        adj = collections.defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        
        pq = [(0, n)] 

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, weight in adj[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))

        dp = [0] * (n + 1)
        dp[n] = 1 

        nodes_sorted_by_dist = sorted(range(1, n + 1), key=lambda x: dist[x])

        for u in nodes_sorted_by_dist:
            for v, weight in adj[u]:
                if dist[u] > dist[v]:
                    dp[u] = (dp[u] + dp[v]) % MOD
        
        return dp[1]

```