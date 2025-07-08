class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        # Step 1 & 2: Rotate the box 90 degrees clockwise
        # The new grid will have n rows and m columns.
        # An element at (r, c) in the original boxGrid moves to (c, m - 1 - r) in the rotated_grid.
        rotated_grid = [['.' for _ in range(m)] for _ in range(n)]

        for r in range(m):
            for c in range(n):
                rotated_grid[c][m - 1 - r] = boxGrid[r][c]

        # Step 3: Apply gravity to the rotated grid
        # Gravity acts downwards, meaning stones fall towards increasing row index in rotated_grid.
        # We process each column independently.
        for j in range(m):  # Iterate through each column of the rotated_grid
            # empty_slot_row tracks the lowest available position for a falling stone in the current column
            # It starts at the very bottom of the column (n-1)
            empty_slot_row = n - 1 
            
            # Iterate from the bottom of the column upwards
            for i in range(n - 1, -1, -1):
                if rotated_grid[i][j] == '#':
                    # If it's a stone, move it to the current empty_slot_row.
                    # If the stone is already at the empty_slot_row (i.e., it's at its lowest possible position
                    # or on top of another stone/obstacle), no actual "move" is needed, just update empty_slot_row.
                    if i != empty_slot_row:
                        rotated_grid[empty_slot_row][j] = '#'
                        rotated_grid[i][j] = '.'
                    # Decrement empty_slot_row as this position is now occupied by a stone.
                    empty_slot_row -= 1
                elif rotated_grid[i][j] == '*':
                    # If it's an obstacle, it stops stones above it.
                    # The next empty_slot_row for stones above this obstacle will be just above it.
                    empty_slot_row = i - 1
                # If it's '.', do nothing, it's already empty.
        
        return rotated_grid