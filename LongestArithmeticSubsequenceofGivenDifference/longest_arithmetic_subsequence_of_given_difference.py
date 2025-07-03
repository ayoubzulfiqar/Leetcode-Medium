class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        # dp dictionary to store the length of the longest arithmetic subsequence
        # ending with a particular number.
        # dp[num] = length of the longest arithmetic subsequence ending with 'num'.
        dp = {}
        
        # Initialize max_len to 0. Since arr.length >= 1, the minimum
        # possible length of an arithmetic subsequence is 1 (any single element).
        # This will be updated to at least 1 in the loop.
        max_len = 0

        # Iterate through each number in the input array
        for num in arr:
            # Calculate the value of the previous element that would form an
            # arithmetic sequence with 'num' given the 'difference'.
            prev_num = num - difference
            
            # Check if 'prev_num' exists in our dp table.
            # If it does, it means we can extend an existing arithmetic subsequence.
            if prev_num in dp:
                # The length of the subsequence ending at 'num' would be
                # the length of the subsequence ending at 'prev_num' plus 1.
                current_length = dp[prev_num] + 1
            else:
                # If 'prev_num' is not in dp, it means 'num' cannot extend
                # any previously found arithmetic subsequence of the given difference.
                # In this case, 'num' itself forms a new arithmetic subsequence of length 1.
                current_length = 1
            
            # Update the dp table: store the calculated 'current_length' for 'num'.
            # If 'num' has appeared before, this will update its stored length
            # to the longest one found so far ending with 'num'.
            dp[num] = current_length
            
            # Update the overall maximum length found across all subsequences.
            max_len = max(max_len, current_length)
        
        # Return the maximum length found.
        return max_len