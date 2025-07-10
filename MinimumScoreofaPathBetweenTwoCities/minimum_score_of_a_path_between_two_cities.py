import collections

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        adj = collections.defaultdict(list)
        for u, v, dist in roads:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        q = collections.deque([1])
        visited.add(1)

        component_nodes = set()
        while q:
            node = q.popleft()
            component_nodes.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        
        min_overall_score = float('inf')
        for u, v, dist in roads:
            if u in component_nodes and v in component_nodes:
                min_overall_score = min(min_overall_score, dist)
        
        return min_overall_score