import collections

class Solution:
    def detonateBombs(self, bombs: list[list[int]]) -> int:
        n = len(bombs)
        
        adj = collections.defaultdict(list)
        
        for i in range(n):
            xi, yi, ri = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj, rj = bombs[j]
                
                dist_sq = (xi - xj)**2 + (yi - yj)**2
                
                if dist_sq <= ri**2:
                    adj[i].append(j)
        
        max_detonated = 0
        
        for i in range(n):
            visited = set()
            stack = [i]
            visited.add(i)
            
            current_detonated_count = 0
            
            while stack:
                u = stack.pop()
                current_detonated_count += 1
                
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        stack.append(v)
            
            max_detonated = max(max_detonated, current_detonated_count)
            
        return max_detonated