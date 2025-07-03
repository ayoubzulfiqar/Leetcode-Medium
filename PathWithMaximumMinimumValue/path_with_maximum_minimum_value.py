import collections

class Solution:
    def maximumMinimumPath(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        low = 0
        high = min(grid[0][0], grid[rows-1][cols-1])
        
        ans = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(val: int) -> bool:
            if grid[0][0] < val: 
                return False
            
            queue = collections.deque([(0, 0)])
            visited = set([(0, 0)])

            while queue:
                r, c = queue.popleft()

                if r == rows - 1 and c == cols - 1:
                    return True 

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] >= val:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            
            return False 

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid 
                low = mid + 1
            else:
                high = mid - 1 

        return ans