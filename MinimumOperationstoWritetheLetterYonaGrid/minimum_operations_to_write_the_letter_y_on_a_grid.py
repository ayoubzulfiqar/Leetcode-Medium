class Solution:
    def minimumOperationsToWriteY(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        is_y_cell = set()
        center_r = n // 2
        center_c = n // 2
        
        for r in range(center_r + 1):
            is_y_cell.add((r, r))
        
        for r in range(center_r + 1):
            is_y_cell.add((r, n - 1 - r))
            
        for r in range(center_r, n):
            is_y_cell.add((r, center_c))
            
        y_cells_values = []
        non_y_cells_values = []
        
        for r in range(n):
            for c in range(n):
                if (r, c) in is_y_cell:
                    y_cells_values.append(grid[r][c])
                else:
                    non_y_cells_values.append(grid[r][c])
                    
        min_ops = float('inf')
        possible_values = [0, 1, 2]
        
        for val_Y in possible_values:
            for val_NonY in possible_values:
                if val_Y == val_NonY:
                    continue
                
                current_ops = 0
                
                for val in y_cells_values:
                    if val != val_Y:
                        current_ops += 1
                        
                for val in non_y_cells_values:
                    if val != val_NonY:
                        current_ops += 1
                
                min_ops = min(min_ops, current_ops)
                
        return min_ops