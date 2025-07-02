class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        is_mine = [[False] * n for _ in range(n)]
        for r, c in mines:
            is_mine[r][c] = True

        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        up = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if is_mine[r][c]:
                    left[r][c] = 0
                    up[r][c] = 0
                else:
                    left[r][c] = (left[r][c-1] + 1) if c > 0 else 1
                    up[r][c] = (up[r-1][c] + 1) if r > 0 else 1

        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if is_mine[r][c]:
                    right[r][c] = 0
                    down[r][c] = 0
                else:
                    right[r][c] = (right[r][c+1] + 1) if c < n - 1 else 1
                    down[r][c] = (down[r+1][c] + 1) if r < n - 1 else 1

        max_order = 0
        for r in range(n):
            for c in range(n):
                current_order = min(left[r][c], right[r][c], up[r][c], down[r][c])
                max_order = max(max_order, current_order)

        return max_order