import bisect

class Solution:
    def waysToSplit(self, nums: list[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        P = [0] * (n + 1)
        for i in range(n):
            P[i+1] = P[i] + nums[i]

        total_ways = 0

        # Iterate through all possible ending positions for the left subarray (index i)
        # The left subarray is nums[0...i]
        # The mid subarray is nums[i+1...j]
        # The right subarray is nums[j+1...n-1]

        # Constraints on indices:
        # 1. left must be non-empty: i >= 0
        # 2. mid must be non-empty: i + 1 <= j
        # 3. right must be non-empty: j + 1 <= n - 1  => j <= n - 2

        # Combining 2 and 3: i + 1 <= j <= n - 2
        # This implies i + 1 <= n - 2  => i <= n - 3
        # So, i ranges from 0 to n - 3.
        for i in range(n - 2):
            s1 = P[i+1] # Sum of the left subarray (nums[0...i])

            # Conditions for the sums:
            # 1. s1 <= s2  => P[i+1] <= (P[j+1] - P[i+1]) => 2 * P[i+1] <= P[j+1]
            # 2. s2 <= s3  => (P[j+1] - P[i+1]) <= (P[n] - P[j+1]) => 2 * P[j+1] <= P[n] + P[i+1]

            # Let k = j+1. The valid range for j is [i+1, n-2].
            # So, the valid range for k is [i+2, n-1].
            # We are looking for indices k in P such that P[k] satisfies the conditions.

            # Calculate the required bounds for P[k] (which is sum of left + mid)
            lower_bound_Pk = 2 * s1
            upper_bound_Pk = (P[n] + s1) // 2 # Integer division is fine here as sums are non-negative

            # Use bisect_left to find the first index k (j+1) in P
            # such that P[k] is greater than or equal to lower_bound_Pk.
            # The search range for k is [i+2, n-1].
            # In bisect_left(a, x, lo, hi), lo is inclusive, hi is exclusive.
            # So, search in P[i+2 ... n-1] means lo=i+2, hi=n (since P has n+1 elements, P[0]...P[n]).
            start_k_idx = bisect.bisect_left(P, lower_bound_Pk, i + 2, n)

            # Use bisect_right to find the first index k (j+1) in P
            # such that P[k] is strictly greater than upper_bound_Pk.
            # The search range is again [i+2, n-1].
            end_k_idx = bisect.bisect_right(P, upper_bound_Pk, i + 2, n)
            
            # The number of valid k values (and thus valid j values) is end_k_idx - start_k_idx.
            # If no valid k values are found, end_k_idx might be less than start_k_idx,
            # so we take max(0, ...) to ensure non-negative count.
            valid_splits_for_i = max(0, end_k_idx - start_k_idx)
            
            total_ways = (total_ways + valid_splits_for_i) % MOD

        return total_ways