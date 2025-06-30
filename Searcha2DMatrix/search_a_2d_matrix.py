class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        
        n = len(matrix[0])
        if n == 0:
            return False

        low = 0
        high = m * n - 1

        while low <= high:
            mid = (low + high) // 2
            
            # Convert the 1D index 'mid' to 2D coordinates (row, col)
            row = mid // n
            col = mid % n
            
            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1
            else: # mid_val > target
                high = mid - 1
        
        return False