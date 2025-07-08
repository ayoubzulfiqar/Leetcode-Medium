import math

class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        total_sum = 0
        neg_count = 0
        min_abs_val = math.inf

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                val = matrix[r][c]
                total_sum += abs(val)
                if val < 0:
                    neg_count += 1
                min_abs_val = min(min_abs_val, abs(val))
        
        if neg_count % 2 == 0:
            return total_sum
        else:
            return total_sum - 2 * min_abs_val