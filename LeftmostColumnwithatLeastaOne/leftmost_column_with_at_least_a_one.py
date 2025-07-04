class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        
        leftmost_col = -1
        
        r = 0
        c = cols - 1
        
        while r < rows and c >= 0:
            if binaryMatrix.get(r, c) == 1:
                leftmost_col = c
                c -= 1
            else:
                r += 1
                
        return leftmost_col