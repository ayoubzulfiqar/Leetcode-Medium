class Solution:
    def countSubmatrices(self, grid: list[list[str]]) -> int:
        M = len(grid)
        N = len(grid[0])

        prefix_x = [[0] * (N + 1) for _ in range(M + 1)]
        prefix_y = [[0] * (N + 1) for _ in range(M + 1)]

        for r in range(M):
            for c in range(N):
                current_x_val = 1 if grid[r][c] == 'X' else 0
                current_y_val = 1 if grid[r][c] == 'Y' else 0

                prefix_x[r+1][c+1] = current_x_val + prefix_x[r][c+1] + prefix_x[r+1][c] - prefix_x[r][c]
                prefix_y[r+1][c+1] = current_y_val + prefix_y[r][c+1] + prefix_y[r+1][c] - prefix_y[r][c]

        count = 0
        for r in range(M):
            for c in range(N):
                num_x = prefix_x[r+1][c+1]
                num_y = prefix_y[r+1][c+1]

                if num_x == num_y and num_x > 0:
                    count += 1
        
        return count