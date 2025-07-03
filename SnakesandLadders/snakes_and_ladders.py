import collections

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        n2 = n * n

        def get_coords(square_num: int) -> tuple[int, int]:
            """
            Converts a 1-indexed square number to its 0-indexed (row, col)
            coordinates on the board, following Boustrophedon style.
            """
            # Convert to 0-indexed square number for easier calculations
            s_idx = square_num - 1

            # Determine the row index from the top (0-indexed)
            # row_from_top = 0 corresponds to the bottom row (n-1)
            # row_from_top = 1 corresponds to the second bottom row (n-2), etc.
            row_from_top = s_idx // n

            # Calculate the actual row index in the board matrix
            r = n - 1 - row_from_top

            # Determine the column index based on the row's direction
            # Even rows from the top (0, 2, ...) go left-to-right
            # Odd rows from the top (1, 3, ...) go right-to-left
            if row_from_top % 2 == 0:
                c = s_idx % n
            else:
                c = n - 1 - (s_idx % n)
            
            return r, c

        # BFS queue: stores tuples of (current_square, moves_taken)
        q = collections.deque([(1, 0)]) 
        
        # Set to keep track of visited squares to avoid cycles and redundant computations
        visited = {1}

        while q:
            curr_square, moves = q.popleft()

            # If we reached the final square, return the number of moves
            if curr_square == n2:
                return moves

            # Simulate rolling a 6-sided die
            for die_roll in range(1, 7):
                next_square = curr_square + die_roll

                # Ensure the next square is within the board limits
                if next_square > n2:
                    continue

                # Get the board coordinates for the next_square
                r, c = get_coords(next_square)
                
                # Check the value at these coordinates on the board
                board_value = board[r][c]

                # Determine the final destination after this roll
                if board_value != -1:
                    # If there's a snake or ladder, move to its destination
                    final_destination = board_value
                else:
                    # Otherwise, move to the square determined by the die roll
                    final_destination = next_square
                
                # If this final_destination has not been visited yet, add it to the queue
                if final_destination not in visited:
                    visited.add(final_destination)
                    q.append((final_destination, moves + 1))

        # If the queue becomes empty and n2 was not reached, it's not possible
        return -1