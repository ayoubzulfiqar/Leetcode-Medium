import collections

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        adj = collections.defaultdict(list)
        for u, v in connections:
            adj[u].append((v, 1))
            adj[v].append((u, 0))
        
        reorientations = 0
        visited = [False] * n
        
        q = collections.deque()
        q.append(0)
        visited[0] = True
        
        while q:
            u = q.popleft()
            
            for v, cost in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    reorientations += cost
                    q.append(v)
                    
        return reorientations