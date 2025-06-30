from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return

        m, n = len(rooms), len(rooms[0])
        
        INF = 2147483647 
        GATE = 0         
        WALL = -1        

        q = deque()

        for r in range(m):
            for c in range(n):
                if rooms[r][c] == GATE:
                    q.append((r, c))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            r, c = q.popleft()
            
            current_dist = rooms[r][c]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    if rooms[nr][nc] == INF:
                        rooms[nr][nc] = current_dist + 1
                        q.append((nr, nc))