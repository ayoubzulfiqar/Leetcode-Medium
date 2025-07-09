class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        row_counts = {}
        for r_idx in range(n):
            row_tuple = tuple(grid[r_idx])
            row_counts[row_tuple] = row_counts.get(row_tuple, 0) + 1
            
        equal_pairs_count = 0
        
        for c_idx in range(n):
            current_col_list = []
            for r_idx in range(n):
                current_col_list.append(grid[r_idx][c_idx])
            
            col_tuple = tuple(current_col_list)
            
            if col_tuple in row_counts:
                equal_pairs_count += row_counts[col_tuple]
                
        return equal_pairs_count