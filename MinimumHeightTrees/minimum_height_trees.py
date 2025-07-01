import collections

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        adj = collections.defaultdict(list)
        degree = [0] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

        q = collections.deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        remaining_nodes = n
        
        while remaining_nodes > 2:
            num_leaves_in_current_layer = len(q)
            remaining_nodes -= num_leaves_in_current_layer

            for _ in range(num_leaves_in_current_layer):
                u = q.popleft()
                for v in adj[u]:
                    degree[v] -= 1
                    if degree[v] == 1:
                        q.append(v)
        
        return list(q)