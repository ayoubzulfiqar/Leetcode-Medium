import collections

class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        q = collections.deque()
        
        found_first_island = False
        
        def dfs(r, c):
            if not (0 <= r < n and 0 <= c < n) or grid[r][c] != 1:
                return
            
            grid[r][c] = 2
            q.append((r, c))
            
            for dr, dc in directions:
                dfs(r + dr, c + dc)
                
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found_first_island = True
                    break
            if found_first_island:
                break
                
        distance = 0
        while q:
            level_size = len(q)
            for _ in range(level_size):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            return distance
                        elif grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
            
            distance += 1
        
        return -1