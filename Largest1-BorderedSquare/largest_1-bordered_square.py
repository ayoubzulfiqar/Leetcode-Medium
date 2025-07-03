class Solution:
    def largest1BorderedSquare(self, grid: list[list[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        dp_right = [[0] * N for _ in range(M)]
        dp_down = [[0] * N for _ in range(M)]

        for r in range(M - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                if grid[r][c] == 1:
                    dp_right[r][c] = 1 + (dp_right[r][c + 1] if c + 1 < N else 0)
                    dp_down[r][c] = 1 + (dp_down[r + 1][c] if r + 1 < M else 0)
                else:
                    dp_right[r][c] = 0
                    dp_down[r][c] = 0

        for k in range(min(M, N), 0, -1):
            for r in range(M - k + 1):
                for c in range(N - k + 1):
                    if (dp_right[r][c] >= k and
                        dp_right[r + k - 1][c] >= k and
                        dp_down[r][c] >= k and
                        dp_down[r][c + k - 1] >= k):
                        return k * k

        return 0