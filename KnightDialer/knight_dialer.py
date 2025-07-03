class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7

        # next_moves[digit] lists the digits that can be reached from 'digit' by a knight's move.
        # Due to the symmetric nature of a knight's move, this dictionary also implicitly defines
        # which digits can jump TO a specific digit. For example, to land on 0, the knight must
        # have come from 4 or 6.
        next_moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],  # The digit 5 has no valid knight moves to or from it.
                    # It can be a starting digit for a number of length 1,
                    # but cannot be part of any number longer than 1.
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        # dp[i] stores the number of distinct phone numbers of the current length
        # that end with digit `i`.
        # For n=1, any of the 10 digits (0-9) can be the starting digit,
        # forming a number of length 1.
        dp = [1] * 10 

        # Iterate from length 2 up to n.
        # Each iteration calculates the counts for the next length based on the current `dp` (previous length).
        for _ in range(2, n + 1):
            new_dp = [0] * 10  # Initialize new_dp for the current length, all counts start at 0.
            
            # Iterate through each possible ending digit (j) for the current length.
            for j in range(10):
                if j == 5:
                    # As per the problem's diagram and knight move rules,
                    # no knight move can land on 5, and 5 has no outgoing moves.
                    # Thus, if a number ends in 5, its length must be 1.
                    # For any length > 1, the count of numbers ending in 5 will be 0.
                    continue 

                # To find the number of ways to end on digit `j` for the current length,
                # sum up the ways to end on `prev_digit` for the previous length,
                # where `prev_digit` can make a valid knight's move to `j`.
                for prev_digit in next_moves[j]:
                    new_dp[j] = (new_dp[j] + dp[prev_digit]) % MOD
            
            # Update dp to be the newly calculated counts for the current length.
            dp = new_dp
        
        # The total number of distinct phone numbers of length n is the sum of
        # the counts of numbers ending on each valid digit after n-1 jumps (total length n).
        total_count = 0
        for count in dp:
            total_count = (total_count + count) % MOD
        
        return total_count