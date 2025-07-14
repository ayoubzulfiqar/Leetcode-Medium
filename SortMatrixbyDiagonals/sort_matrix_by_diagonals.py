import collections

class Solution:
    def sort_matrix_by_diagonals(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        
        diagonals = collections.defaultdict(list)
        
        for r in range(n):
            for c in range(n):
                diagonals[r - c].append(grid[r][c])
        
        for diag_id in diagonals:
            if diag_id >= 0:
                diagonals[diag_id].sort(reverse=True)
            else:
                diagonals[diag_id].sort()
        
        result_grid = [[0] * n for _ in range(n)]
        
        diag_indices = collections.defaultdict(int)
        
        for r in range(n):
            for c in range(n):
                diag_id = r - c
                result_grid[r][c] = diagonals[diag_id][diag_indices[diag_id]]
                diag_indices[diag_id] += 1
                
        return result_grid