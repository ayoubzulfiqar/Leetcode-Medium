class KnightTour:
    def __init__(self, N):
        self.N = N
        self.board = [[-1 for _ in range(N)] for _ in range(N)]
        self.x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
        self.y_moves = [1, 2, 2, 1, -1, -2, -2, -1]

    def _is_safe(self, x, y):
        return 0 <= x < self.N and 0 <= y < self.N and self.board[x][y] == -1

    def _solve_tour_util(self, x, y, move_count):
        if move_count == self.N * self.N:
            return True

        for i in range(8):
            next_x = x + self.x_moves[i]
            next_y = y + self.y_moves[i]

            if self._is_safe(next_x, next_y):
                self.board[next_x][next_y] = move_count + 1
                if self._solve_tour_util(next_x, next_y, move_count + 1):
                    return True
                self.board[next_x][next_y] = -1
        return False

    def solve(self, start_x=0, start_y=0):
        if not (0 <= start_x < self.N and 0 <= start_y < self.N):
            print("Invalid starting position.")
            return False

        self.board[start_x][start_y] = 1

        if self._solve_tour_util(start_x, start_y, 1):
            for row in self.board:
                print(" ".join(f"{cell:2d}" for cell in row))
            return True
        else:
            print("Solution does not exist for the given board size and starting position.")
            return False

if __name__ == "__main__":
    board_size = 8
    knight_tour = KnightTour(board_size)
    knight_tour.solve(0, 0)