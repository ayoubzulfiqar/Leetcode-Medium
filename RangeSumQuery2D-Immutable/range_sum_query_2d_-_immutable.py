class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0

        self.prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                self.prefix_sum[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.prefix_sum[r][c + 1]
                    + self.prefix_sum[r + 1][c]
                    - self.prefix_sum[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        sum_bottom_right = self.prefix_sum[row2 + 1][col2 + 1]
        sum_above = self.prefix_sum[row1][col2 + 1]
        sum_left = self.prefix_sum[row2 + 1][col1]
        sum_top_left_corner = self.prefix_sum[row1][col1]

        return sum_bottom_right - sum_above - sum_left + sum_top_left_corner