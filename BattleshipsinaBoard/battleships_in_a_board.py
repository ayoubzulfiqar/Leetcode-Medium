from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])

        battleship_count = 0

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    # Check if this 'X' is the top-leftmost cell of a battleship.
                    # A cell is the top-leftmost if:
                    # 1. It's an 'X'.
                    # 2. There is no 'X' directly above it (or it's in the first row).
                    # 3. There is no 'X' directly to its left (or it's in the first column).

                    # Check if there's an 'X' immediately above (i.e., board[i-1][j] is 'X')
                    if i > 0 and board[i-1][j] == 'X':
                        continue # This 'X' is part of a battleship extending downwards from above.

                    # Check if there's an 'X' immediately to the left (i.e., board[i][j-1] is 'X')
                    if j > 0 and board[i][j-1] == 'X':
                        continue # This 'X' is part of a battleship extending rightwards from the left.
                    
                    # If neither of the above conditions is true, it means this 'X' is
                    # the top-left corner of a new, uncounted battleship.
                    battleship_count += 1
        
        return battleship_count