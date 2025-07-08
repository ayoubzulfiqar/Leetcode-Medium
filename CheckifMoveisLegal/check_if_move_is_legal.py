import collections
from typing import List

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        opponent_color = 'W' if color == 'B' else 'B'
        
        directions = [
            (-1, -1), (-1, 0), (-1, 1), # Up-left, Up, Up-right
            (0, -1),           (0, 1),   # Left, Right
            (1, -1), (1, 0), (1, 1)    # Down-left, Down, Down-right
        ]
        
        for dr, dc in directions:
            curr_r, curr_c = rMove + dr, cMove + dc
            opponent_count = 0
            
            while 0 <= curr_r < 8 and 0 <= curr_c < 8:
                cell_content = board[curr_r][curr_c]
                
                if cell_content == opponent_color:
                    opponent_count += 1
                    curr_r += dr
                    curr_c += dc
                elif cell_content == color:
                    if opponent_count >= 1:
                        return True
                    else:
                        break 
                else: # cell_content == '.'
                    break
        
        return False