class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        word_len = len(word)

        def dfs(r, c, k):
            if k == word_len:
                return True

            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[k]:
                return False

            original_char = board[r][c]
            board[r][c] = '#'

            found = (dfs(r + 1, c, k + 1) or
                     dfs(r - 1, c, k + 1) or
                     dfs(r, c + 1, k + 1) or
                     dfs(r, c - 1, k + 1))

            board[r][c] = original_char

            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        return False