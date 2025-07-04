import collections

class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        
        diagonal_map = collections.defaultdict(list)
        
        # Populate the dictionary with diagonal elements
        for r in range(m):
            for c in range(n):
                diagonal_map[r - c].append(mat[r][c])
        
        # Sort each diagonal's elements
        for diff in diagonal_map:
            diagonal_map[diff].sort()
            
        # Place sorted elements back into the matrix
        for r in range(m):
            for c in range(n):
                mat[r][c] = diagonal_map[r - c].pop(0)
                
        return mat