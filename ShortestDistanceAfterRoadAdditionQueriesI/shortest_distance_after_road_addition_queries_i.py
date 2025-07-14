import collections

class Solution:
    def shortestDistanceAfterRoadAdditionQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        adj = collections.defaultdict(list)

        for i in range(n - 1):
            adj[i].append(i + 1)

        results = []

        for u, v in queries:
            adj[u].append(v)

            q = collections.deque([(0, 0)])
            
            dist = [-1] * n
            dist[0] = 0

            while q:
                curr_node, curr_dist = q.popleft()

                if curr_node == n - 1:
                    results.append(curr_dist)
                    break

                for neighbor in adj[curr_node]:
                    if dist[neighbor] == -1:
                        dist[neighbor] = curr_dist + 1
                        q.append((neighbor, curr_dist + 1))
                
        return results