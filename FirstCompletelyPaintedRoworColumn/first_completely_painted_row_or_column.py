class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        num_to_pos = {}
        for r in range(m):
            for c in range(n):
                num_to_pos[mat[r][c]] = (r, c)

        row_painted_count = [0] * m
        col_painted_count = [0] * n

        for i, num in enumerate(arr):
            r, c = num_to_pos[num]

            row_painted_count[r] += 1
            col_painted_count[c] += 1

            if row_painted_count[r] == n:
                return i

            if col_painted_count[c] == m:
                return i

        return -1