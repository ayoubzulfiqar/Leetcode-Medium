import collections

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        adj = [[] for _ in range(n)]
        for i in range(n):
            if manager[i] != -1:
                adj[manager[i]].append(i)
        
        queue = collections.deque([(headID, 0)]) 
        
        max_total_time = 0
        
        while queue:
            u, current_informed_time = queue.popleft()
            
            max_total_time = max(max_total_time, current_informed_time)
            
            for v in adj[u]:
                queue.append((v, current_informed_time + informTime[u]))
                
        return max_total_time