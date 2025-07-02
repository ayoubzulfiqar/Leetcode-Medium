import random

def solve(board):
    """
    Simulates the Candy Crush game process until no more matches can be made.

    Args:
        board (list[list[int]]): The initial game board, where each element
                                 represents a candy type (positive integer)
                                 or an empty space (0).

    Returns:
        list[list[int]]: The final stable state of the board after all
                         possible crushes, gravity applications, and refills.
    """
    R = len(board)
    if R == 0:
        return board
    C = len(board[0])
    if C == 0:
        return board

    while True:
        # Step 1: Find and mark matches
        # This function modifies the board in place by setting matched candies to 0.
        matched_found = find_matches(board)

        # If no matches were found in this pass, the board is stable.
        if not matched_found:
            break

        # Step 2: Apply gravity
        # Candies fall down to fill empty spaces.
        apply_gravity(board)

        # Step 3: Fill new candies
        # New random candies fill the empty spaces at the top.
        fill_new_candies(board)

    return board

def find_matches(board):
    """
    Identifies all horizontal and vertical matches of 3 or more identical candies.
    Marks matched candies by setting their value to 0 (empty).

    Args:
        board (list[list[int]]): The current game board.

    Returns:
        bool: True if any matches were found and crushed, False otherwise.
    """
    R, C = len(board), len(board[0])
    to_crush = set()  # Stores (row, col) coordinates of candies to be crushed
    any_match_found = False

    # Horizontal scan for matches
    for r in range(R):
        for c in range(C - 2):
            val = board[r][c]
            # A match requires at least 3 identical, non-empty candies in a row
            if val != 0 and val == board[r][c+1] and val == board[r][c+2]:
                any_match_found = True
                to_crush.add((r, c))
                to_crush.add((r, c+1))
                to_crush.add((r, c+2))
                # Extend the match to the right if more identical candies exist
                k = 3
                while c + k < C and board[r][c+k] == val:
                    to_crush.add((r, c+k))
                    k += 1

    # Vertical scan for matches
    for c in range(C):
        for r in range(R - 2):
            val = board[r][c]
            # A match requires at least 3 identical, non-empty candies in a column
            if val != 0 and val == board[r+1][c] and val == board[r+2][c]:
                any_match_found = True
                to_crush.add((r, c))
                to_crush.add((r+1, c))
                to_crush.add((r+2, c))
                # Extend the match downwards if more identical candies exist
                k = 3
                while r + k < R and board[r+k][c] == val:
                    to_crush.add((r+k, c))
                    k += 1

    # Apply crushing: set all marked candies to 0
    for r, c in to_crush:
        board[r][c] = 0

    return any_match_found

def apply_gravity(board):
    """
    Applies gravity to the board, causing candies to fall down and fill empty spaces.
    Empty spaces (0s) will float to the top of each column.

    Args:
        board (list[list[int]]): The current game board, modified in place.
    """
    R, C = len(board), len(board[0])

    for c in range(C):  # Process each column independently
        write_idx = R - 1  # Pointer for where to place the next non-empty candy (starts from bottom)
        
        # Iterate from the bottom of the column upwards
        for read_idx in range(R - 1, -1, -1):
            if board[read_idx][c] != 0:
                # If a candy is found, move it to the current write_idx position
                board[write_idx][c] = board[read_idx][c]
                write_idx -= 1  # Move write_idx up to the next available slot

        # After moving all candies, fill the remaining top cells with 0s
        # write_idx now points to the highest row that should be empty
        for r in range(write_idx, -1, -1):
            board[r][c] = 0

def fill_new_candies(board):
    """
    Fills all empty spaces (0s) on the board with new random candy types.
    Assumes candy types are integers from 1 to 5.

    Args:
        board (list[list[int]]): The current game board, modified in place.
    """
    R, C = len(board), len(board[0])
    
    for r in range(R):
        for c in range(C):
            if board[r][c] == 0:
                # Replace empty space with a random candy type (e.g., 1 to 5)
                board[r][c] = random.randint(1, 5)