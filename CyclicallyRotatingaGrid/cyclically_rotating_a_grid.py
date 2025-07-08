class Solution:
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2

        for layer_idx in range(num_layers):
            r1, c1 = layer_idx, layer_idx
            r2, c2 = m - 1 - layer_idx, n - 1 - layer_idx

            current_layer_elements = []

            # Extract elements in counter-clockwise order
            # Top row (left to right)
            for j in range(c1, c2 + 1):
                current_layer_elements.append(grid[r1][j])
            
            # Right column (top to bottom, excluding top-right)
            for i in range(r1 + 1, r2 + 1):
                current_layer_elements.append(grid[i][c2])
            
            # Bottom row (right to left, excluding bottom-right)
            if r1 != r2: 
                for j in range(c2 - 1, c1 - 1, -1):
                    current_layer_elements.append(grid[r2][j])
            
            # Left column (bottom to top, excluding bottom-left and top-left)
            if c1 != c2: 
                for i in range(r2 - 1, r1, -1):
                    current_layer_elements.append(grid[i][c1])
            
            layer_length = len(current_layer_elements)
            
            if layer_length == 0:
                continue
            
            effective_k = k % layer_length
            
            rotated_layer_elements = current_layer_elements[effective_k:] + current_layer_elements[:effective_k]
            
            # Place elements back into the grid
            element_idx = 0

            # Top row (left to right)
            for j in range(c1, c2 + 1):
                grid[r1][j] = rotated_layer_elements[element_idx]
                element_idx += 1
            
            # Right column (top to bottom, excluding top-right)
            for i in range(r1 + 1, r2 + 1):
                grid[i][c2] = rotated_layer_elements[element_idx]
                element_idx += 1
            
            # Bottom row (right to left, excluding bottom-right)
            if r1 != r2:
                for j in range(c2 - 1, c1 - 1, -1):
                    grid[r2][j] = rotated_layer_elements[element_idx]
                    element_idx += 1
            
            # Left column (bottom to top, excluding bottom-left and top-left)
            if c1 != c2:
                for i in range(r2 - 1, r1, -1):
                    grid[i][c1] = rotated_layer_elements[element_idx]
                    element_idx += 1
                    
        return grid