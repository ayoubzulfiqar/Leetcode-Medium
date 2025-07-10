class Solution:
    def maxStarSum(self, vals: list[int], edges: list[list[int]], k: int) -> int:
        n = len(vals)
        
        adj = [[] for _ in range(n)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        max_star_sum = -float('inf')
        
        if n > 0:
            max_star_sum = max(vals) 
        else: # Should not happen based on constraints (1 <= n)
            return 0 

        for i in range(n):
            current_center_val = vals[i]
            
            positive_neighbor_vals = []
            for neighbor_node in adj[i]:
                if vals[neighbor_node] > 0:
                    positive_neighbor_vals.append(vals[neighbor_node])
            
            positive_neighbor_vals.sort(reverse=True)
            
            current_star_sum = current_center_val
            
            for j in range(min(k, len(positive_neighbor_vals))):
                current_star_sum += positive_neighbor_vals[j]
            
            max_star_sum = max(max_star_sum, current_star_sum)
            
        return max_star_sum