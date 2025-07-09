class Solution:
    def numberOfHiddenSequences(self, differences: list[int], lower: int, upper: int) -> int:
        current_sum = 0
        min_prefix_sum = 0
        max_prefix_sum = 0

        for diff in differences:
            current_sum += diff
            min_prefix_sum = min(min_prefix_sum, current_sum)
            max_prefix_sum = max(max_prefix_sum, current_sum)
        
        # The hidden sequence is h[0], h[0] + p[1], h[0] + p[2], ..., h[0] + p[n]
        # where p[i] is the prefix sum of differences up to differences[i-1], and p[0] = 0.
        # So, h[i] = h[0] + prefix_sum[i].
        # We need lower <= h[i] <= upper for all i.
        # This means lower <= h[0] + prefix_sum[i] <= upper.
        # Rearranging for h[0]:
        # lower - prefix_sum[i] <= h[0] <= upper - prefix_sum[i]

        # For this to hold for all i, h[0] must satisfy:
        # max(lower - prefix_sum[i]) <= h[0] <= min(upper - prefix_sum[i])

        # This is equivalent to:
        # lower - min(prefix_sum[i]) <= h[0] <= upper - max(prefix_sum[i])
        # (Because subtracting a smaller number results in a larger lower bound,
        # and subtracting a larger number results in a smaller upper bound.)

        # Our min_prefix_sum and max_prefix_sum variables already capture min(prefix_sum[i]) and max(prefix_sum[i])
        # across all i from 0 to n (where prefix_sum[0] is implicitly 0).

        # The minimum possible value for h[0] is lower - max_val_relative_to_h0
        # The maximum possible value for h[0] is upper - min_val_relative_to_h0
        # This is incorrect based on my derivation above. Let's re-verify.

        # lower <= h[0] + p_i  => h[0] >= lower - p_i. To satisfy all, h[0] >= max(lower - p_i) = lower - min(p_i).
        # h[0] + p_i <= upper  => h[0] <= upper - p_i. To satisfy all, h[0] <= min(upper - p_i) = upper - max(p_i).

        # So, the valid range for h[0] is [lower - min_prefix_sum, upper - max_prefix_sum].
        
        # The number of integers in a range [A, B] is B - A + 1.
        # If B < A, there are no integers, so the count is 0.
        
        count = (upper - max_prefix_sum) - (lower - min_prefix_sum) + 1
        
        return max(0, count)