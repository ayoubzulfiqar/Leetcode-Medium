class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0.0] * n for _ in range(n)] for _ in range(k + 1)]

        dp[0][row][column] = 1.0

        moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]

        for s in range(k):
            for r in range(n):
                for c in range(n):
                    if dp[s][r][c] > 0:
                        for dr, dc in moves:
                            next_r, next_c = r + dr, c + dc
                            if 0 <= next_r < n and 0 <= next_c < n:
                                dp[s + 1][next_r][next_c] += dp[s][r][c] / 8.0

        total_probability_on_board = 0.0
        for r in range(n):
            for c in range(n):
                total_probability_on_board += dp[k][r][c]

        return total_probability_on_board