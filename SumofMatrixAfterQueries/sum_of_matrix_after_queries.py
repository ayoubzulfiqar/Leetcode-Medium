class Solution:
    def matrixSumQueries(self, n: int, queries: list[list[int]]) -> int:
        total_sum = 0
        
        row_covered = [False] * n
        col_covered = [False] * n
        
        covered_rows_count = 0
        covered_cols_count = 0
        
        for i in range(len(queries) - 1, -1, -1):
            query_type, index, val = queries[i]
            
            if query_type == 0:  # Row query
                if not row_covered[index]:
                    total_sum += val * (n - covered_cols_count)
                    row_covered[index] = True
                    covered_rows_count += 1
            else:  # Column query (query_type == 1)
                if not col_covered[index]:
                    total_sum += val * (n - covered_rows_count)
                    col_covered[index] = True
                    covered_cols_count += 1
            
            if covered_rows_count == n and covered_cols_count == n:
                break
                
        return total_sum