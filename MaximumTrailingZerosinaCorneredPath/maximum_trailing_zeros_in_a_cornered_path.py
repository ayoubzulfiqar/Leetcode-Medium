class Solution:
    def maxTrailingZeros(self, grid: list[list[int]]) -> int:
        def count_factors(n, factor):
            count = 0
            while n > 0 and n % factor == 0:
                count += 1
                n //= factor
            return count

        m, n = len(grid), len(grid[0])

        twos_grid = [[0] * n for _ in range(m)]
        fives_grid = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                twos_grid[r][c] = count_factors(val, 2)
                fives_grid[r][c] = count_factors(val, 5)

        dp_twos_left = [[0] * n for _ in range(m)]
        dp_fives_left = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                dp_twos_left[r][c] = twos_grid[r][c]
                dp_fives_left[r][c] = fives_grid[r][c]
                if c > 0:
                    dp_twos_left[r][c] += dp_twos_left[r][c-1]
                    dp_fives_left[r][c] += dp_fives_left[r][c-1]

        dp_twos_right = [[0] * n for _ in range(m)]
        dp_fives_right = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n - 1, -1, -1):
                dp_twos_right[r][c] = twos_grid[r][c]
                dp_fives_right[r][c] = fives_grid[r][c]
                if c < n - 1:
                    dp_twos_right[r][c] += dp_twos_right[r][c+1]
                    dp_fives_right[r][c] += dp_fives_right[r][c+1]

        dp_twos_up = [[0] * n for _ in range(m)]
        dp_fives_up = [[0] * n for _ in range(m)]
        for c in range(n):
            for r in range(m):
                dp_twos_up[r][c] = twos_grid[r][c]
                dp_fives_up[r][c] = fives_grid[r][c]
                if r > 0:
                    dp_twos_up[r][c] += dp_twos_up[r-1][c]
                    dp_fives_up[r][c] += dp_fives_up[r-1][c]

        dp_twos_down = [[0] * n for _ in range(m)]
        dp_fives_down = [[0] * n for _ in range(m)]
        for c in range(n):
            for r in range(m - 1, -1, -1):
                dp_twos_down[r][c] = twos_grid[r][c]
                dp_fives_down[r][c] = fives_grid[r][c]
                if r < m - 1:
                    dp_twos_down[r][c] += dp_twos_down[r+1][c]
                    dp_fives_down[r][c] += dp_fives_down[r+1][c]

        max_zeros = 0

        for r in range(m):
            for c in range(n):
                current_twos = twos_grid[r][c]
                current_fives = fives_grid[r][c]

                # Path Left -> (r,c) -> Down
                twos = dp_twos_left[r][c] + dp_twos_down[r][c] - current_twos
                fives = dp_fives_left[r][c] + dp_fives_down[r][c] - current_fives
                max_zeros = max(max_zeros, min(twos, fives))

                # Path Left -> (r,c) -> Up
                twos = dp_twos_left[r][c] + dp_twos_up[r][c] - current_twos
                fives = dp_fives_left[r][c] + dp_fives_up[r][c] - current_fives
                max_zeros = max(max_zeros, min(twos, fives))

                # Path Right -> (r,c) -> Down
                twos = dp_twos_right[r][c] + dp_twos_down[r][c] - current_twos
                fives = dp_fives_right[r][c] + dp_fives_down[r][c] - current_fives
                max_zeros = max(max_zeros, min(twos, fives))

                # Path Right -> (r,c) -> Up
                twos = dp_twos_right[r][c] + dp_twos_up[r][c] - current_twos
                fives = dp_fives_right[r][c] + dp_fives_up[r][c] - current_fives
                max_zeros = max(max_