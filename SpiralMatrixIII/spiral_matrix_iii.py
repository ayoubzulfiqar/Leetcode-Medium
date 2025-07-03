class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        ans = []
        
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        
        r, c = rStart, cStart
        d_idx = 0
        
        steps = 1
        
        if 0 <= r < rows and 0 <= c < cols:
            ans.append([r, c])
        
        while len(ans) < rows * cols:
            for _ in range(2):
                for _ in range(steps):
                    r += dr[d_idx]
                    c += dc[d_idx]
                    
                    if 0 <= r < rows and 0 <= c < cols:
                        ans.append([r, c])
                    
                    if len(ans) == rows * cols:
                        return ans
                
                d_idx = (d_idx + 1) % 4
            
            steps += 1
            
        return ans