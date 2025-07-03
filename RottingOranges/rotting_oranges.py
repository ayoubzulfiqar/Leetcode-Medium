import collections

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        q = collections.deque()
        fresh_oranges = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
                    
        minutes = 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q and fresh_oranges > 0:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        q.append((nr, nc))
            
            if q: 
                minutes += 1
        
        if fresh_oranges == 0:
            return minutes
        else:
            return -1