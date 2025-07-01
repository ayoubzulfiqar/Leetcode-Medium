class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows_count = [[0] * n for _ in range(3)]
        self.cols_count = [[0] * n for _ in range(3)]
        self.diag1_count = [0] * 3
        self.diag2_count = [0] * 3

    def move(self, row: int, col: int, player: int) -> int:
        self.rows_count[player][row] += 1
        self.cols_count[player][col] += 1

        if row == col:
            self.diag1_count[player] += 1
        
        if row + col == self.n - 1:
            self.diag2_count[player] += 1
        
        if self.rows_count[player][row] == self.n or \
           self.cols_count[player][col] == self.n or \
           self.diag1_count[player] == self.n or \
           self.diag2_count[player] == self.n:
            return player
        else:
            return 0