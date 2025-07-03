class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1):
            temp_dist = list(dist)
            for u, v, price in flights:
                if dist[u] != float('inf'):
                    temp_dist[v] = min(temp_dist[v], dist[u] + price)
            dist = temp_dist
        
        if dist[dst] == float('inf'):
            return -1
        else:
            return dist[dst]