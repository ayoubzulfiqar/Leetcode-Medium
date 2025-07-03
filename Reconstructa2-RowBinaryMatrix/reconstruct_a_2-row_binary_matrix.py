class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: list[int]) -> list[list[int]]:
        n = len(colsum)
        
        matrix = [[0] * n for _ in range(2)]
        
        for i in range(n):
            if colsum[i] == 2:
                matrix[0][i] = 1
                matrix[1][i] = 1
                upper -= 1
                lower -= 1
        
        if upper < 0 or lower < 0:
            return []
            
        for i in range(n):
            if colsum[i] == 1:
                if upper > 0:
                    matrix[0][i] = 1
                    upper -= 1
                else:
                    matrix[1][i] = 1
                    lower -= 1
        
        if upper == 0 and lower == 0:
            return matrix
        else:
            return []