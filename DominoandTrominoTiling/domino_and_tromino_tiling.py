class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        # f_prev2: Represents f[i-2], the number of ways to tile a full 2x(i-2) board.
        # f_prev1: Represents f[i-1], the number of ways to tile a full 2x(i-1) board.
        # g_prev2: Represents g[i-2], the number of ways to tile a 2x(i-2) board with the top-right cell missing.
        # g_prev1: Represents g[i-1], the number of ways to tile a 2x(i-1) board with the top-right cell missing.

        # Base cases:
        # For a 2x0 board (empty): 1 way (f[0] = 1)
        # For a 2x1 board: 1 way (one vertical domino) (f[1] = 1)
        # For partial boards:
        # A 2x0 board cannot have a missing cell (g[0] = 0)
        # A 2x1 board cannot have a missing cell (g[1] = 0)

        f_prev2 = 1  # Corresponds to f[0]
        f_prev1 = 1  # Corresponds to f[1]
        g_prev2 = 0  # Corresponds to g[0]
        g_prev1 = 0  # Corresponds to g[1]

        # Iterate from i = 2 up to n
        for i in range(2, n + 1):
            # Recurrence for f[i]:
            # 1. Add a vertical domino: f[i-1] ways
            # 2. Add two horizontal dominoes: f[i-2] ways
            # 3. Add two types of trominoes that complete the board from a partial (g[i-1]) state: 2 * g[i-1] ways
            f_curr = (f_prev1 + f_prev2 + 2 * g_prev1) % MOD

            # Recurrence for g[i]:
            # (where g[i] is a 2xi board with top-right cell missing)
            # 1. Add a horizontal domino to the bottom row, completing f[i-1]: f[i-1] ways
            # 2. Add a tromino that extends from a g[i-2] state: g[i-2] ways
            g_curr = (f_prev1 + g_prev2) % MOD

            # Update variables for the next iteration
            f_prev2 = f_prev1
            f_prev1 = f_curr
            g_prev2 = g_prev1
            g_prev1 = g_curr

        # If n=1, the loop range(2, 2) is empty, and f_prev1 (initialized to 1) is returned.
        # For n >= 2, f_prev1 will hold the calculated f[n].
        return f_prev1