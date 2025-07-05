class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        max_area = 0
        
        current_heights = [0] * n 

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 1:
                    current_heights[c] += 1
                else:
                    current_heights[c] = 0

            sorted_heights = sorted(current_heights, reverse=True)

            for i in range(n):
                current_area = sorted_heights[i] * (i + 1)
                max_area = max(max_area, current_area)
        
        return max_area