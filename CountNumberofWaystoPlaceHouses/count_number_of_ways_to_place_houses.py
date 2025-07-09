class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9 + 7

        # For a single side of the street with 'k' plots,
        # let dp[k] be the number of ways to place houses such that
        # no two houses are adjacent.
        #
        # Base cases:
        # dp[0] = 1 (There's one way to place houses on 0 plots: place nothing)
        # dp[1] = 2 (For 1 plot, either place a house or leave it empty: [H], [E])
        #
        # Recurrence relation for k > 1:
        # If the k-th plot is empty (E): The previous k-1 plots can be arranged in dp[k-1] ways.
        # If the k-th plot has a house (H): The (k-1)-th plot MUST be empty (E).
        #                                   The previous k-2 plots can be arranged in dp[k-2] ways.
        # So, dp[k] = dp[k-1] + dp[k-2].
        # This is a Fibonacci-like sequence.

        # We need to calculate dp[n] for one side.
        # We can compute this iteratively with O(1) space.
        
        # 'ways_n_minus_2' stores dp[i-2]
        # 'ways_n_minus_1' stores dp[i-1]
        ways_n_minus_2 = 1  # Corresponds to dp[0]
        ways_n_minus_1 = 2  # Corresponds to dp[1]

        # The loop calculates dp[i] from i=2 up to n.
        # If n=1, the loop range(2, 1+1) which is range(2,2) will not execute.
        # In this case, ways_n_minus_1 correctly holds dp[1] (which is 2).
        for _ in range(2, n + 1):
            current_ways_one_side = (ways_n_minus_1 + ways_n_minus_2) % MOD
            ways_n_minus_2 = ways_n_minus_1
            ways_n_minus_1 = current_ways_one_side
        
        # After the loop, 'ways_n_minus_1' holds dp[n],
        # the number of ways to place houses on 'n' plots for one side of the street.
        
        # Since there are two independent sides of the street,
        # the total number of ways is (ways for one side) * (ways for the other side).
        total_ways = (ways_n_minus_1 * ways_n_minus_1) % MOD
        
        return total_ways