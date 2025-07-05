class Solution:
    def countSubmatrices(self, mat: list[list[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        
        # height[i][j] stores the number of consecutive ones ending at (i, j) upwards
        # (i.e., the height of the column of ones ending at (i, j))
        height = [[0] * n for _ in range(m)]
        
        total_submatrices = 0
        
        # Iterate through each cell of the matrix
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    # If the current cell is 1, calculate its height
                    if i == 0:
                        height[i][j] = 1
                    else:
                        height[i][j] = height[i-1][j] + 1
                    
                    # Now, consider (i, j) as the bottom-right corner of submatrices.
                    # We iterate leftwards from column j to 0.
                    # For each column k, we find the minimum height in the range [k, j].
                    # This minimum height determines how many valid rectangles of width (j - k + 1)
                    # can be formed with (i, j) as the bottom-right corner.
                    min_h = height[i][j]
                    for k in range(j, -1, -1):
                        # Update min_h with the height of the current column k.
                        # This ensures min_h is the smallest height in the current horizontal slice [k, j].
                        min_h = min(min_h, height[i][k])
                        
                        # Add min_h to the total count.
                        # min_h represents the number of submatrices of width (j - k + 1)
                        # and heights from 1 to min_h that end at (i, j).
                        total_submatrices += min_h
                else:
                    # If mat[i][j] is 0, no submatrix of all ones can end here.
                    # So, its height is 0.
                    height[i][j] = 0
        
        return total_submatrices