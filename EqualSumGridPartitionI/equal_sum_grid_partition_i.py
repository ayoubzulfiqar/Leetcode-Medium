class Solution:
    def canPartition(self, grid: list[list[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        total_sum = 0
        for r in range(m):
            for c in range(n):
                total_sum += grid[r][c]

        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2

        current_horizontal_sum = 0
        for r_idx in range(m - 1):
            for c_idx in range(n):
                current_horizontal_sum += grid[r_idx][c_idx]
            if current_horizontal_sum == target_sum:
                return True

        current_vertical_sum = 0
        for c_idx in range(n - 1):
            for r_idx in range(m):
                current_vertical_sum += grid[r_idx][c_idx]
            if current_vertical_sum == target_sum:
                return True

        return False