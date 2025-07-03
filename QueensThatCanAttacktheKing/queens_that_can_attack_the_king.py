class Solution:
    def queensAttacktheKing(self, queens: list[list[int]], king: list[int]) -> list[list[int]]:
        
        queen_positions = set(tuple(q) for q in queens)
        
        kx, ky = king[0], king[1]
        
        attacking_queens = []
        
        directions = [
            (-1, 0), (1, 0),
            (0, -1), (0, 1),
            (-1, -1), (1, 1),
            (-1, 1), (1, -1)
        ]
        
        for dx, dy in directions:
            current_x, current_y = kx + dx, ky + dy
            
            while 0 <= current_x < 8 and 0 <= current_y < 8:
                if (current_x, current_y) in queen_positions:
                    attacking_queens.append([current_x, current_y])
                    break 
                
                current_x += dx
                current_y += dy
                
        return attacking_queens