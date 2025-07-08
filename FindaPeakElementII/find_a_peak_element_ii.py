class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        m = len(mat)
        n = len(mat[0])

        low_col = 0
        high_col = n - 1

        while low_col <= high_col:
            mid_col = low_col + (high_col - low_col) // 2

            # Find the row with the maximum element in the current mid_col
            max_row = 0
            for r in range(m):
                if mat[r][mid_col] > mat[max_row][mid_col]:
                    max_row = r
            
            current_val = mat[max_row][mid_col]

            # Get the value of the left neighbor, handling boundary with -1 perimeter
            left_val = -1
            if mid_col > 0:
                left_val = mat[max_row][mid_col - 1]
            
            # Get the value of the right neighbor, handling boundary with -1 perimeter
            right_val = -1
            if mid_col < n - 1:
                right_val = mat[max_row][mid_col + 1]
            
            # Check if current_val is a peak
            # It's already the maximum in its column (thus greater than top/bottom neighbors within the column).
            # We just need to check left and right neighbors.
            if current_val > left_val and current_val > right_val:
                return [max_row, mid_col]
            elif current_val < left_val:
                # If the left neighbor is greater, a peak must be in the left half of columns.
                high_col = mid_col - 1
            else: # current_val < right_val
                # If the right neighbor is greater, a peak must be in the right half of columns.
                low_col = mid_col + 1
        
        # This line should theoretically not be reached as the problem guarantees a peak exists.
        return [-1, -1]

```