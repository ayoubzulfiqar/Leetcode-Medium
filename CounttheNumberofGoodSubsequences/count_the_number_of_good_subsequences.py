class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        target = "0123456789"
        MOD = 10**9 + 7

        # dp[i] will store the number of subsequences of s that match
        # the prefix target[0...i-1].
        # dp[0] = 1 represents one way to form an empty prefix (the empty subsequence).
        dp = [0] * (len(target) + 1)
        dp[0] = 1

        for char_s in s:
            # Convert the character from the input string to an integer digit.
            # This assumes the input string `s` contains only digits '0'-'9'.
            digit_s = int(char_s)
            
            # Iterate backwards through the target string.
            # This ensures that when we update dp[k], dp[k-1] refers to the count
            # calculated using characters processed *before* the current char_s,
            # preventing double-counting or using the current char_s multiple times
            # for different parts of the same subsequence.
            for k in range(len(target), 0, -1):
                # Get the digit at the current position in the target sequence.
                target_digit = int(target[k-1])
                
                # If the current digit from the input string matches the target digit
                # for the current position in the target sequence:
                if digit_s == target_digit:
                    # We can extend all subsequences that form target[0...k-2]
                    # by appending the current digit_s to form target[0...k-1].
                    # Add the number of ways to form target[0...k-2] (dp[k-1])
                    # to the current count of ways to form target[0...k-1] (dp[k]).
                    dp[k] = (dp[k] + dp[k-1]) % MOD
        
        # The final result is the number of ways to form the complete target string
        # "0123456789", which is stored in dp[len(target)].
        return dp[len(target)]