class Solution:
    def isValidTicTacToeBoard(self, board: list[str]) -> bool:
        x_count = 0
        o_count = 0
        for row in board:
            for char in row:
                if char == 'X':
                    x_count += 1
                elif char == 'O':
                    o_count += 1

        def check_win(player_char: str) -> bool:
            # Check rows
            for i in range(3):
                if all(board[i][j] == player_char for j in range(3)):
                    return True
            # Check columns
            for j in range(3):
                if all(board[i][j] == player_char for i in range(3)):
                    return True
            # Check diagonals
            if all(board[i][i] == player_char for i in range(3)):
                return True
            if all(board[i][2-i] == player_char for i in range(3)):
                return True
            return False

        x_wins = check_win('X')
        o_wins = check_win('O')

        # Rule 1: Basic turn counts
        # O cannot have more moves than X
        if o_count > x_count:
            return False
        # X cannot have two or more moves than O
        if x_count > o_count + 1:
            return False

        # Rule 2: Both players cannot win
        if x_wins and o_wins:
            return False

        # Rule 3: If X wins, X must have exactly one more piece than O
        # (X made the winning move, so it must have been X's turn)
        if x_wins:
            if x_count == o_count: # This implies O moved after X won, or X won on O's turn
                return False

        # Rule 4: If O wins, X and O must have the same number of pieces
        # (O made the winning move, so it must have been O's turn)
        if o_wins:
            if x_count == o_count + 1: # This implies X moved after O won, or O won on X's turn
                return False

        # If all checks pass, the board is valid
        return True