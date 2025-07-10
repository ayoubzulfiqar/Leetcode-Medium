import collections

class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        safeness_grid = [[-1] * n for _ in range(n)]
        q = collections.deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    safeness_grid[r][c] = 0
                    q.append((r, c))
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q:
            r, c = q.popleft()
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < n and safeness_grid[nr][nc] == -1:
                    safeness_grid[nr][nc] = safeness_grid[r][c] + 1
                    q.append((nr, nc))
        
        low = 0
        high = 2 * n 
        ans = 0
        
        def can_reach(k: int) -> bool:
            if safeness_grid[0][0] < k:
                return False
            
            bfs_q = collections.deque()
            bfs_q.append((0, 0))
            
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
            
            while bfs_q:
                r, c = bfs_q.popleft()
                
                if r == n - 1 and c == n - 1:
                    return True
                
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and safeness_grid[nr][nc] >= k:
                        visited[nr][nc] = True
                        bfs_q.append((nr, nc))
            
            return False

        while low <= high:
            mid = low + (high - low) // 2
            if can_reach(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans