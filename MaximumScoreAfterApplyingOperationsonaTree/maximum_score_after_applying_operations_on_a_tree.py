import collections

class Solution:
    def maximumScoreAfterOperations(self, edges: list[list[int]], values: list[int]) -> int:
        n = len(values)
        
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        total_sum_values = sum(values)
        
        def dfs(u, parent):
            is_leaf = True
            sum_of_children_min_unpicked = 0
            
            for v in adj[u]:
                if v == parent:
                    continue
                is_leaf = False
                sum_of_children_min_unpicked += dfs(v, u)
            
            if is_leaf:
                return values[u]
            else:
                return min(values[u], sum_of_children_min_unpicked)
        
        min_unpicked_sum = dfs(0, -1)
        
        return total_sum_values - min_unpicked_sum