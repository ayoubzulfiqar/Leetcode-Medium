import heapq

class Solution:
    def max_sum_with_at_most_k_elements(self, grid: list[list[int]], limits: list[int], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        max_sum = 0
        
        pq = [] 
        
        sorted_grid_rows = []
        for i in range(n):
            sorted_row = sorted(grid[i], reverse=True)
            sorted_grid_rows.append(sorted_row)
            
            if limits[i] > 0:
                heapq.heappush(pq, (-sorted_row[0], i, 0))
        
        current_indices = [0] * n 
        
        for _ in range(k):
            if not pq:
                break
            
            neg_val, row_idx, _ = heapq.heappop(pq)
            val = -neg_val
            
            max_sum += val
            
            current_indices[row_idx] += 1
            
            if current_indices[row_idx] < limits[row_idx] and \
               current_indices[row_idx] < m:
                
                next_val = sorted_grid_rows[row_idx][current_indices[row_idx]]
                heapq.heappush(pq, (-next_val, row_idx, current_indices[row_idx]))
                
        return max_sum