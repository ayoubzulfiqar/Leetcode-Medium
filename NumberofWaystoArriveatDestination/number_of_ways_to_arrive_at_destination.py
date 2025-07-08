import heapq

class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v, time in roads:
            adj[u].append((v, time))
            adj[v].append((u, time))

        dist = [float('inf')] * n
        ways = [0] * n
        
        dist[0] = 0
        ways[0] = 1
        
        # Min-heap stores (current_time, node)
        pq = [(0, 0)] 
        
        MOD = 10**9 + 7
        
        while pq:
            d, u = heapq.heappop(pq)
            
            # If we found a shorter path to u already, skip this outdated entry
            if d > dist[u]:
                continue
                
            for v, time_uv in adj[u]:
                new_dist = d + time_uv
                
                if new_dist < dist[v]:
                    # Found a strictly shorter path to v
                    dist[v] = new_dist
                    ways[v] = ways[u] # All previous ways to v are now invalid
                    heapq.heappush(pq, (new_dist, v))
                elif new_dist == dist[v]:
                    # Found another path with the same shortest time to v
                    ways[v] = (ways[v] + ways[u]) % MOD
                    
        return ways[n-1]