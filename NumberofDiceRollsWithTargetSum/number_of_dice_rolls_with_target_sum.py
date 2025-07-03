class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        # dp[i][j] will store the number of ways to get sum j using i dice.
        # i ranges from 0 to n (number of dice)
        # j ranges from 0 to target (current sum)
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        # Base case: With 0 dice, there is 1 way to get a sum of 0 (by doing nothing).
        dp[0][0] = 1

        # Iterate through the number of dice from 1 to n
        for i in range(1, n + 1):
            # Iterate through possible sums from 1 to target
            for j in range(1, target + 1):
                # For the current die (the i-th die), try all possible face values from 1 to k
                for face in range(1, k + 1):
                    # If the current sum 'j' can be formed by rolling 'face' on the i-th die,
                    # and the remaining (i-1) dice formed the sum (j - face).
                    # We need to ensure that (j - face) is a non-negative sum.
                    if j - face >= 0:
                        # Add the ways to achieve (j - face) with (i-1) dice to the current ways
                        # for (i) dice and sum (j).
                        dp[i][j] = (dp[i][j] + dp[i-1][j-face]) % MOD

        # The result is the number of ways to get 'target' sum using 'n' dice.
        return dp[n][target]