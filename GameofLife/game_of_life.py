class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        m = len(board)
        n = len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        # First pass: Update board with intermediate states
        # 0: dead -> dead (original state was 0)
        # 1: live -> live (original state was 1)
        # 2: live -> dead (original state was 1, will become 0)
        # 3: dead -> live (original state was 0, will become 1)
        for r in range(m):
            for c in range(n):
                live_neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        # A neighbor is considered 'live' for the current generation's calculation
                        # if its original state was 1 (represented by 1 or 2)
                        if board[nr][nc] == 1 or board[nr][nc] == 2:
                            live_neighbors += 1
                
                current_state = board[r][c]

                if current_state == 1: # Currently live
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2 # Live cell dies (under-population or over-population)
                    # Else (2 or 3 live neighbors), it lives, so board[r][c] remains 1
                else: # Currently dead (current_state == 0)
                    if live_neighbors == 3:
                        board[r][c] = 3 # Dead cell becomes live (reproduction)
                    # Else, it remains dead, so board[r][c] remains 0

        # Second pass: Convert intermediate states to final 0s and 1s
        for r in range(m):
            for c in range(n):
                if board[r][c] == 2: # Was live, now dead
                    board[r][c] = 0
                elif board[r][c] == 3: # Was dead, now live
                    board[r][c] = 1

```