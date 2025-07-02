class Solution:
    def findLonelyPixel(self, picture: list[list[str]], N: int) -> int:
        rows = len(picture)
        if rows == 0:
            return 0
        cols = len(picture[0])
        if cols == 0:
            return 0

        row_counts = [0] * rows
        for r in range(rows):
            for c in range(cols):
                if picture[r][c] == 'B':
                    row_counts[r] += 1

        row_strings = ["".join(picture[r]) for r in range(rows)]

        lonely_pixels = 0

        for c in range(cols):
            b_rows_in_col = []
            for r in range(rows):
                if picture[r][c] == 'B':
                    b_rows_in_col.append(r)

            if len(b_rows_in_col) == N:
                all_rows_have_one_B = True
                for r_idx in b_rows_in_col:
                    if row_counts[r_idx] != 1:
                        all_rows_have_one_B = False
                        break

                if all_rows_have_one_B:
                    first_row_pattern = row_strings[b_rows_in_col[0]]
                    all_rows_are_identical = True
                    for r_idx in b_rows_in_col:
                        if row_strings[r_idx] != first_row_