class Vector2D:

    def __init__(self, vec: list[list[int]]):
        self.vec = vec
        self.row_idx = 0
        self.col_idx = 0

    def next(self) -> int:
        # It's assumed that next() is called only when hasNext() is True.
        # This means self.row_idx and self.col_idx are already pointing
        # to a valid element.
        val = self.vec[self.row_idx][self.col_idx]
        self.col_idx += 1
        return val

    def hasNext(self) -> bool:
        # Advance row_idx and col_idx until a valid element is found
        # or the end of the vector is reached.
        while self.row_idx < len(self.vec):
            if self.col_idx < len(self.vec[self.row_idx]):
                # Found a valid element at current (row_idx, col_idx)
                return True
            
            # Current row is exhausted or empty, move to the next row
            self.row_idx += 1
            self.col_idx = 0 # Reset column index for the new row
            
        # All rows have been processed, no more elements
        return False

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()