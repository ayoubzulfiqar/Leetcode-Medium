class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m = len(mat)
        n = len(mat[0])

        result = []
        r, c = 0, 0
        
        # True for up-right direction, False for down-left direction
        direction_up = True 

        # Loop until all elements are added to the result
        while len(result) < m * n:
            # Add the current element to the result list
            result.append(mat[r][c])

            if direction_up:
                # Attempt to move up-right: (r-1, c+1)
                next_r, next_c = r - 1, c + 1
                
                # Check boundary conditions for the next move
                if next_c >= n: # Hit the right wall
                    # Move down to the next row, change direction
                    r += 1 
                    direction_up = False
                elif next_r < 0: # Hit the top wall
                    # Move right to the next column, change direction
                    c += 1 
                    direction_up = False
                else: # Valid up-right move
                    # Update current position
                    r, c = next_r, next_c
            else: # direction_up is False, meaning moving down-left
                # Attempt to move down-left: (r+1, c-1)
                next_r, next_c = r + 1, c - 1

                # Check boundary conditions for the next move
                if next_r >= m: # Hit the bottom wall
                    # Move right to the next column, change direction
                    c += 1 
                    direction_up = True
                elif next_c < 0: # Hit the left wall
                    # Move down to the next row, change direction
                    r += 1 
                    direction_up = True
                else: # Valid down-left move
                    # Update current position
                    r, c = next_r, next_c
        
        return result