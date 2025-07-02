from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])
        clickr, clickc = click[0], click[1]

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        if board[clickr][clickc] == 'M':
            board[clickr][clickc] = 'X'
            return board

        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n) or board[r][c] != 'E':
                return

            mine_count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    mine_count += 1

            if mine_count > 0:
                board[r][c] = str(mine_count)
            else:
                board[r][c] = 'B'
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    dfs(nr, nc)

        dfs(clickr, clickc)
        return board