import itertools

class Solution:
    def maximumRows(self, matrix: list[list[int]], numSelect: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        max_covered_rows = 0
        
        column_indices = range(n)
        
        for selected_column_indices in itertools.combinations(column_indices, numSelect):
            current_covered_rows = 0
            selected_cols_set = set(selected_column_indices)
            
            for r in range(m):
                row_is_covered = True
                for c in range(n):
                    if matrix[r][c] == 1:
                        if c not in selected_cols_set:
                            row_is_covered = False
                            break
                
                if row_is_covered:
                    current_covered_rows += 1
            
            max_covered_rows = max(max_covered_rows, current_covered_rows)
            
        return max_covered_rows