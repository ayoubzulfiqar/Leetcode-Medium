import math

class Solution:
    def minSplitIntoSubarraysWithGCDGreaterThanOne(self, nums: list[int]) -> int:
        # If the array contains the number 1, it's impossible to satisfy the condition.
        # Any subarray containing 1 will have a GCD of 1, which is not greater than 1.
        # A subarray consisting solely of [1] also has a GCD of 1.
        if 1 in nums:
            return -1

        n = len(nums)
        if n == 0:
            return 0

        # dp[i] stores the minimum number of subarrays required to partition the prefix nums[0...i-1].
        # dp[0] is 0, as an empty prefix requires no subarrays.
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # Iterate through each possible end index `i` (from 1 to n) for the current prefix.
        # `i` represents the length of the prefix `nums[0...i-1]`.
        for i in range(1, n + 1):
            # `current_gcd_val` will store the GCD of the subarray `nums[j...i-1]`.
            current_gcd_val = 0 

            # Iterate backwards from `j = i-1` down to `0`.
            # `j` represents the starting index of the last subarray `nums[j...i-1]`.
            for j in range(i - 1, -1, -1):
                # If `j` is `i-1`, the subarray is just `[nums[i-1]]`.
                # Otherwise, we extend the current subarray `nums[j+1...i-1]` by including `nums[j]`.
                if j == i - 1:
                    current_gcd_val = nums[i-1]
                else:
                    current_gcd_val = math.gcd(current_gcd_val, nums[j])

                # If the GCD of the current subarray `nums[j...i-1]` is greater than 1,
                # then this subarray is a valid candidate for the last split.
                if current_gcd_val > 1:
                    # If the prefix `nums[0...j-1]` was reachable (i.e., `dp[j]` is not infinity),
                    # we can potentially form a valid partition ending at `i-1`.
                    if dp[j] != float('inf'):
                        # Update `dp[i]` with the minimum number of splits:
                        # `dp[j]` (minimum splits for `nums[0...j-1]`) + 1 (for the current valid subarray `nums[j...i-1]`).
                        dp[i] = min(dp[i], dp[j] + 1)
        
        # The final result is `dp[n]`, which represents the minimum splits for the entire array `nums[0...n-1]`.
        # If `1` is not present in `nums`, a solution always exists (at worst, each element forms its own subarray).
        return dp[n]