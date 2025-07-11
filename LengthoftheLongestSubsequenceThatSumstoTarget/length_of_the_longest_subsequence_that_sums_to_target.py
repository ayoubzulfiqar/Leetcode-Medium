class Solution:
    def longestSubsequence(self, nums: list[int], target: int) -> int:
        # dp[s] will store the maximum length of a subsequence that sums up to s.
        # Initialize dp array with -1, indicating no such subsequence found yet.
        # dp[0] is 0 because an empty subsequence sums to 0 and has length 0.
        dp = [-1] * (target + 1)
        dp[0] = 0

        # Iterate through each number in nums
        for num in nums:
            # Iterate backwards from target down to num.
            # This ensures that each number `num` is used at most once in a subsequence.
            # If we iterated forwards, `num` could be used multiple times
            # (e.g., dp[s] updated using dp[s - num], and then dp[s - num]
            # might have been updated using the same `num` in the current iteration).
            for s in range(target, num - 1, -1):
                # If s - num is achievable (i.e., dp[s - num] is not -1),
                # then we can form a sum `s` by adding `num` to a subsequence
                # that sums to `s - num`.
                if dp[s - num] != -1:
                    # Update dp[s] with the maximum length found so far.
                    # This is either the current dp[s] or dp[s - num] + 1
                    # (adding `num` increases the length by 1).
                    dp[s] = max(dp[s], dp[s - num] + 1)

        # The result is the maximum length for the target sum.
        # If dp[target] is still -1, it means no subsequence sums to target.
        return dp[target]