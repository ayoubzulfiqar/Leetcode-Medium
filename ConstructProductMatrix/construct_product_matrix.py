class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        MOD = 12345
        
        n = len(grid)
        m = len(grid[0])
        N = n * m # Total number of elements
        
        # prefix_products[k] will store the product of elements from index 0 to k-1 (flattened)
        # suffix_products[k] will store the product of elements from index k+1 to N-1 (flattened)
        prefix_products = [1] * N
        suffix_products = [1] * N
        
        # Calculate prefix products
        current_prod = 1
        for k in range(N):
            r = k // m
            c = k % m
            prefix_products[k] = current_prod
            current_prod = (current_prod * (grid[r][c] % MOD)) % MOD
        
        # Calculate suffix products
        current_prod = 1
        for k in range(N - 1, -1, -1):
            r = k // m
            c = k % m
            suffix_products[k] = current_prod
            current_prod = (current_prod * (grid[r][c] % MOD)) % MOD
            
        # Construct the product matrix
        product_matrix = [[0] * m for _ in range(n)]
        for k in range(N):
            r = k // m
            c = k % m
            product_matrix[r][c] = (prefix_products[k] * suffix_products[k]) % MOD
            
        return product_matrix