class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        n = len(piles)
        
        # dp[i][j] represents the maximum score difference the current player
        # can achieve over the opponent when considering the subarray piles[i...j].
        dp = [[0] * n for _ in range(n)]
        
        # Base cases: Subarrays of length 1
        # If only one pile is left, the current player takes it.
        # The difference is just the value of that pile.
        for i in range(n):
            dp[i][i] = piles[i]
            
        # Fill the DP table for subarrays of increasing length
        # Length 'length' goes from 2 to n
        for length in range(2, n + 1):
            # 'i' is the starting index of the subarray
            # 'j' is the ending index of the subarray
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Option 1: Current player takes piles[i]
                # The player gets piles[i].
                # The remaining game is on piles[i+1...j].
                # The opponent will play optimally on this remaining subarray,
                # achieving a score difference of dp[i+1][j] (opponent's score - current player's score).
                # So, the current player's score difference from this move is piles[i] - dp[i+1][j].
                score_if_take_left = piles[i] - dp[i+1][j]
                
                # Option 2: Current player takes piles[j]
                # The player gets piles[j].
                # The remaining game is on piles[i...j-1].
                # The opponent will play optimally, achieving dp[i][j-1].
                # So, the current player's score difference from this move is piles[j] - dp[i][j-1].
                score_if_take_right = piles[j] - dp[i][j-1]
                
                # The current player plays optimally to maximize their score difference.
                dp[i][j] = max(score_if_take_left, score_if_take_right)
                
        # Alice is the first player. She wants to maximize her score difference over Bob.
        # The final result dp[0][n-1] represents the maximum score difference Alice can achieve
        # over Bob from the entire array piles[0...n-1].
        # If this difference is positive, Alice wins.
        return dp[0][n-1] > 0