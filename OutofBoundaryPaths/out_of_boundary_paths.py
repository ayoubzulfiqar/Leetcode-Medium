class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        
        dp_curr = [[0] * n for _ in range(m)]
        dp_curr[startRow][startColumn] = 1
        
        ans = 0
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for _ in range(maxMove):
            dp_next = [[0] * n for _ in range(m)]
            
            for r in range(m):
                for c in range(n):
                    if dp_curr[r][c] > 0:
                        for dr, dc in dirs:
                            nr, nc = r + dr, c + dc
                            
                            if nr < 0 or nr >= m or nc < 0 or nc >= n:
                                ans = (ans + dp_curr[r][c]) % MOD
                            else:
                                dp_next[nr][nc] = (dp_next[nr][nc] + dp_curr[r][c]) % MOD
            
            dp_curr = dp_next
            
        return ans