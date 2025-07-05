class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        m = len(grid)
        n = len(grid[0])
        
        answer = [-1] * n
        
        for start_col in range(n):
            current_col = start_col
            
            for row in range(m):
                board_direction = grid[row][current_col]
                
                next_col = current_col + board_direction
                
                if next_col < 0 or next_col >= n:
                    current_col = -1
                    break
                
                if board_direction == 1 and grid[row][next_col] == -1:
                    current_col = -1
                    break
                if board_direction == -1 and grid[row][next_col] == 1:
                    current_col = -1
                    break
                    
                current_col = next_col
            
            answer[start_col] = current_col
            
        return answer