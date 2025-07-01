class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]:
            self.rows = 0
            self.cols = 0
            return

        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.matrix = [[0] * self.cols for _ in range(self.rows)]
        self.bit = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]

        for r in range(self.rows):
            for c in range(self.cols):
                self.update(r, c, matrix[r][c])

    def _update_bit(self, r_idx, c_idx, val):
        r_idx += 1
        c_idx += 1
        
        i = r_idx
        while i <= self.rows:
            j = c_idx
            while j <= self.cols:
                self.bit[i][j] += val
                j += (j & -j)
            i += (i & -i)

    def _query_bit(self, r_idx, c_idx):
        r_idx += 1
        c_idx += 1
        
        total = 0
        i = r_idx
        while i > 0:
            j = c_idx
            while j > 0:
                total += self.bit[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return total

    def update(self, row: int, col: int, val: int) -> None:
        if self.rows == 0 or self.cols == 0:
            return

        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self._update_bit(row, col, diff)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.rows == 0 or self.cols == 0:
            return 0
        
        total = self._query_bit(row2, col2)
        
        if row1 > 0:
            total -= self._query_bit(row1 - 1, col2)
        
        if col1 > 0:
            total -= self._query_bit(row2, col1 - 1)
        
        if row1 > 0 and col1 > 0:
            total += self._query_bit(row1 - 1, col1 - 1)
            
        return total