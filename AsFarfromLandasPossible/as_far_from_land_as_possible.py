import collections

class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        queue = collections.deque()
        has_land = False
        has_water = False
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    has_land = True
                else:
                    has_water = True
        
        if not has_land or not has_water:
            return -1
            
        max_dist = -1
        level = 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc))
                        max_dist = level + 1 
            
            level += 1
            
        return max_dist