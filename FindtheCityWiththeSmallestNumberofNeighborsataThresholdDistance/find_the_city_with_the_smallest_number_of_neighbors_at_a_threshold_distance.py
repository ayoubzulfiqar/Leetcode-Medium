import math

class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        dist = [[math.inf] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for u, v, weight in edges:
            dist[u][v] = min(dist[u][v], weight)
            dist[v][u] = min(dist[v][u], weight)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != math.inf and dist[k][j] != math.inf:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        min_reachable_count = n + 1
        result_city = -1

        for i in range(n):
            current_reachable_count = 0
            for j in range(n):
                if i == j:
                    continue
                if dist[i][j] <= distanceThreshold:
                    current_reachable_count += 1
            
            if current_reachable_count < min_reachable_count:
                min_reachable_count = current_reachable_count
                result_city = i
            elif current_reachable_count == min_reachable_count:
                result_city = max(result_city, i)
                
        return result_city