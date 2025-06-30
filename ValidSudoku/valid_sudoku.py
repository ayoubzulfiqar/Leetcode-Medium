class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                char = board[r][c]
                if char == '.':
                    continue

                # Check row validity
                if char in rows[r]:
                    return False
                rows[r].add(char)

                # Check column validity
                if char in cols[c]:
                    return False
                cols[c].add(char)

                # Check 3x3 sub-box validity
                # Calculate the index of the 3x3 box
                # There are 9 boxes, indexed from 0 to 8
                # box_idx = (row_block_index * 3) + col_block_index
                # row_block_index = r // 3
                # col_block_index = c // 3
                box_idx = (r // 3) * 3 + (c // 3)
                if char in boxes[box_idx]:
                    return False
                boxes[box_idx].add(char)

        return True