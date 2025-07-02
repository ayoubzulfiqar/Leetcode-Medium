```python
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j] will store the minimum money needed to guarantee a win
        # for the numbers in the range [i, j].
        # The dp table uses 1-based indexing for convenience, so its size is (n+1) x (n+1).
        # Initialize all entries to 0.
        # dp[i][i] = 0, as there's only one number, you guess it and pay nothing if correct.
        # dp[i][j] where i > j represents an empty or invalid range, cost is 0.
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Iterate over the length of the range (len_range).
        # A range of length 1 (e.g., [i, i]) has a cost of 0, which is handled by initialization.
        # So we start with ranges of length 2.
        for length in range(2, n + 1):
            # Iterate over the starting point 'i' of the current range.
            # 'j' is the ending point of the range, calculated as 'i + length - 1'.
            # The loop for 'i' goes up to 'n - length + 1' to ensure 'j' does not exceed 'n'.
            for i in range(1, n - length + 2):
                j = i + length - 1
                
                # Initialize dp[i][j] to a very large value (infinity)
                # because we are looking for the minimum cost.
                dp[i][j] = float('inf')
                
                # Iterate over all possible numbers 'k' within the range [i, j]
                # that we could guess first.
                # 'k' is the money we pay for this guess.
                for k in range(i, j + 1):
                    # If the actual number is lower than 'k', the new range is [i, k-1].
                    # The cost for this subproblem is dp[i][k-1].
                    # If k is 'i', then [i, k-1] is an invalid range (e.g., [1,0]),
                    # its cost is considered 0.
                    cost_if_lower = dp[i][k-1] if k > i else 0
                    
                    # If the actual number is higher than 'k', the new range is [k+1, j].
                    # The cost for this subproblem is dp[k+1][j].
                    # If k is 'j', then [k+1, j] is an invalid range (e.g., [11,10] for n=10, k=10),
                    # its cost is considered 0.
                    cost_if_higher = dp[k+1][j] if k < j else 0
                    
                    # To guarantee a win, we must prepare for the worst-case scenario
                    # after guessing 'k'. This means taking the maximum of the costs
                    # for the lower and higher subproblems, and adding 'k' (the cost of the current guess).
                    current_guess_total_cost = k + max(cost_if_lower, cost_if_higher)
                    
                    # We want to find the minimum of these worst-case costs
                    # across all possible initial guesses 'k'.
                    dp[i][j] = min(dp[i][j], current_guess_total_cost)
        
        # The final answer is the minimum money needed to guarantee a win
        # for the entire range [1, n].
        return dp[1][n]

```