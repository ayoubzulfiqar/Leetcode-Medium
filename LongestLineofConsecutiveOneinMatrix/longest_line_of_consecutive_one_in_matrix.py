class Solution:
    def longestLine(self, M: list[list[int]]) -> int:
        if not M or not M[0]:
            return 0

        rows = len(M)
        cols = len(M[0])
        
        # dp[c][dir] stores the length of the longest line of consecutive ones
        # ending at (current_row, c) in direction 'dir'.
        # We use prev_dp to store values from the previous row (r-1).
        # And curr_dp to store values for the current row (r).
        # dir 0: horizontal (from left)
        # dir 1: vertical (from top)
        # dir 2: diagonal (from top-left)
        # dir 3: anti-diagonal (from top-right)
        
        prev_dp = [[0] * 4 for _ in range(cols)]
        max_len = 0

        for r in range(rows):
            curr_dp = [[0] * 4 for _ in range(cols)]
            for c in range(cols):
                if M[r][c] == 1:
                    # Horizontal: depends on (r, c-1) which is in curr_dp
                    curr_dp[c][0] = 1 + (curr_dp[c-1][0] if c > 0 else 0)
                    
                    # Vertical: depends on (r-1, c) which is in prev_dp
                    curr_dp[c][1] = 1 + prev_dp[c][1]
                    
                    # Diagonal: depends on (r-1, c-1) which is in prev_dp
                    curr_dp[c][2] = 1 + (prev_dp[c-1][2] if c > 0 else 0)
                    
                    # Anti-diagonal: depends on (r-1, c+1) which is in prev_dp
                    curr_dp[c][3] = 1 + (prev_dp[c+1][3] if c < cols - 1 else 0)
                    
                    # Update overall maximum length
                    max_len = max(max_len, curr_dp[c][0], curr_dp[c][1], curr_dp[c][2], curr_dp[c][3])
            
            # After processing the current row, update prev_dp for the next iteration
            prev_dp = curr_dp
        
        return max_len