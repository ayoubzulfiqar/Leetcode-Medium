class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        result = []
        
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1
        
        while top <= bottom and left <= right:
            # Traverse right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # Traverse down
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            # Traverse left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            # Traverse up
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
                
        return result