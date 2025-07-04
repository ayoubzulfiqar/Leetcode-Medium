class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        # Calculate the number of trailing zeros for each row
        # A trailing zero is a zero at the end of the row.
        # For example, [1,0,0] has 2 trailing zeros. [0,0,0] has 3 trailing zeros.
        trailing_zeros_count = []
        for r in range(n):
            count = 0
            # Iterate from the rightmost column to the left
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 0:
                    count += 1
                else:
                    # Found a '1', so stop counting trailing zeros
                    break 
            trailing_zeros_count.append(count)
        
        total_swaps = 0
        
        # Iterate through each target row position (from top to bottom, 0 to n-1)
        for i in range(n):
            # For a grid to be valid, row 'i' must have all zeros in columns > i.
            # This means row 'i' must have at least (n - 1 - i) trailing zeros.
            required_zeros = n - 1 - i
            
            # Search for the first available row (starting from current position 'i')
            # that satisfies the requirement of 'required_zeros'.
            found_idx = -1
            for k in range(i, n):
                if trailing_zeros_count[k] >= required_zeros:
                    found_idx = k
                    break
            
            # If no suitable row is found among the remaining ones, it's impossible
            # to make the grid valid.
            if found_idx == -1:
                return -1
            
            # The number of swaps needed to bring the row from 'found_idx' to 'i'
            # is simply the difference in their indices. This is because each swap
            # moves a row one position up.
            total_swaps += (found_idx - i)
            
            # Simulate moving the found row to the current position 'i'.
            # This is done by removing the element at 'found_idx' and inserting it
            # at 'i'. This correctly updates the relative positions of other rows.
            val_to_move = trailing_zeros_count.pop(found_idx)
            trailing_zeros_count.insert(i, val_to_move)
            
        return total_swaps