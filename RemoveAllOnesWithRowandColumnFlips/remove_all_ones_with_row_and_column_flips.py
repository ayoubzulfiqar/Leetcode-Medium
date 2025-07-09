class Solution:
    def removeOnes(self, grid: list[list[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # The first row serves as a reference.
        # We determine the necessary column flips based on the first row
        # (assuming we don't flip the first row itself, R_0 = 0).
        # Then, for every other row, it must either be identical to the
        # first row or its bitwise complement to be transformable to all zeros.

        # Let R_r be 1 if row r is flipped, 0 otherwise.
        # Let C_c be 1 if column c is flipped, 0 otherwise.
        # For a cell grid[r][c] to become 0, we need:
        # (grid[r][c] + R_r + C_c) % 2 == 0
        # Which implies: grid[r][c] == (R_r + C_c) % 2
        # Or using XOR: grid[r][c] ^ R_r ^ C_c == 0
        # So, grid[r][c] == R_r ^ C_c

        # Consider the first row (r=0):
        # grid[0][c] == R_0 ^ C_c
        # If we choose R_0 = 0 (no flip for the first row), then:
        # C_c = grid[0][c] for all c.
        # This means we flip columns where grid[0][c] is 1.

        # Now consider any other row r:
        # grid[r][c] == R_r ^ C_c
        # Substitute C_c = grid[0][c]:
        # grid[r][c] == R_r ^ grid[0][c]
        # This implies: R_r == grid[r][c] ^ grid[0][c]

        # For a given row r, R_r must be a constant value for all columns c.
        # Therefore, grid[r][c] ^ grid[0][c] must be the same for all c in row r.
        # Let this constant value be `expected_xor_value`.
        # `expected_xor_value` will be 0 if row r should be identical to row 0.
        # `expected_xor_value` will be 1 if row r should be the complement of row 0.

        # We can determine `expected_xor_value` for each row `r` by checking its first element:
        # expected_xor_value = grid[r][0] ^ grid[0][0]

        first_row_val = grid[0][0]

        # Iterate through rows starting from the second row (index 1)
        for r in range(m):
            current_row_val = grid[r][0]
            
            # Determine the expected XOR value for this row based on its first element.
            # If grid[r][0] is the same as grid[0][0], then this row must be identical to grid[0].
            # (i.e., grid[r][c] ^ grid[0][c] should be 0 for all c).
            # If grid[r][0] is different from grid[0][0], then this row must be the complement of grid[0].
            # (i.e., grid[r][c] ^ grid[0][c] should be 1 for all c).
            expected_xor_value = current_row_val ^ first_row_val

            # Now, verify this expected relationship for all other elements in the current row.
            for c in range(n):
                if (grid[r][c] ^ grid[0][c]) != expected_xor_value:
                    return False # Mismatch found, impossible to make all zeros

        return True