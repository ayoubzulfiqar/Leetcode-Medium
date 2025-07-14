def minMovesToGetPeacefulBoard(board):
    rows = len(board)
    if rows == 0:
        return 0
    cols = len(board[0])
    if cols == 0:
        return 0

    moves_pattern1 = 0
    for r in range(rows):
        for c in range(cols):
            expected_val = (r + c) % 2
            if board[r][c] != expected_val:
                moves_pattern1 += 1

    moves_pattern2 = 0
    for r in range(rows):
        for c in range(cols):
            expected_val = (r + c + 1) % 2
            if board[r][c] != expected_val:
                moves_pattern2 += 1
    
    return min(moves_pattern1, moves_pattern2)