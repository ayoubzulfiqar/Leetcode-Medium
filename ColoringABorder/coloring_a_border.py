import collections

class Solution:
    def colorBorder(self, grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        start_color = grid[row][col]
        
        q = collections.deque([(row, col)])
        visited = set([(row, col)]) 
        
        cells_to_color = [] 
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q:
            r, c = q.popleft