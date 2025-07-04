class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        R = len(rowSum)
        C = len(colSum)
        
        matrix = [[0] * C for _ in range(R)]
        
        for i in range(R):
            for j in range(C):
                val = min(rowSum[i], colSum[j])
                matrix[i][j] = val
                rowSum[i] -= val
                colSum[j] -= val
                
        return matrix