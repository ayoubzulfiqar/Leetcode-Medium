class BinaryMatrix3D:
    def __init__(self, depth, rows, cols):
        if not (isinstance(depth, int) and depth > 0 and
                isinstance(rows, int) and rows > 0 and
                isinstance(cols, int) and cols > 0):
            raise ValueError("Dimensions (depth, rows, cols) must be positive integers.")

        self.depth = depth
        self.rows = rows
        self.cols = cols
        self.matrix = [[[0 for _ in range(cols)] for _ in range(rows)] for _ in range(depth)]
        self.layer_counts = [0] * depth

    def _validate_coordinates(self, d, r, c):
        if not (0 <= d < self.depth and
                0 <= r < self.rows and
                0 <= c < self.cols):
            raise IndexError(f"Coordinates ({d}, {r}, {c}) are out of bounds for matrix "
                             f"dimensions ({self.depth}, {self.rows}, {self.cols}).")

    def set_cell(self, d, r, c, value):
        self._validate_coordinates(d, r, c)
        if value not in (0, 1):
            raise ValueError("Cell value must be 0 or 1.")

        current_value = self.matrix[d][r][c]

        if current_value != value:
            self.matrix[d][r][c] = value
            if value == 1:
                self.layer_counts[d] += 1
            else:
                self.layer_counts[d] -= 1

    def get_cell(self, d, r, c):
        self._validate_coordinates(d, r, c)
        return self.matrix[d][r][c]

    def get_layer_count(self, d):
        if not (0 <= d < self.depth):
            raise IndexError(f"Depth index {d} is out of bounds for matrix depth {self.depth}.")
        return self.layer_counts[d]