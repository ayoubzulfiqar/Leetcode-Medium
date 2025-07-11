class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        
        current_row0_sum_right = sum(grid[0])
        current_row1_sum_left = 0
        
        min_max_score = float('inf')
        
        for i in range(n):
            current_row0_sum_right -= grid[0][i]
            
            second_robot_score = max(current_row1_sum_left, current_row0_sum_right)
            
            min_max_score = min(min_max_score, second_robot_score)
            
            current_row1_sum_left += grid[1][i]
            
        return min_max_score