class Solution:
    def specialPermutations(self, nums: list[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        # dp[mask][last_idx] stores the number of special permutations
        # using elements represented by 'mask', with nums[last_idx] being the last element.
        # mask is a bitmask where the i-th bit is set if nums[i] is included.
        dp = [[0] * n for _ in range(1 << n)]

        # Base cases: A single element permutation is always special.
        # For each element nums[i], a permutation consisting only of nums[i] has count 1.
        for i in range(n):
            dp[1 << i][i] = 1

        # Iterate through all possible masks (subsets of nums)
        # from masks representing permutations of length 1 up to the full mask (length n).
        for mask in range(1, 1 << n):
            # Iterate through all possible last elements (by their index) for the current mask.
            for last_idx in range(n):
                # Check if nums[last_idx] is part of the current mask AND
                # if there is at least one valid permutation ending with nums[last_idx] for this mask.
                # If dp[mask][last_idx] is 0, it means no valid permutation
                # of elements in 'mask' ends with nums[last_idx], so we cannot extend it.
                if not ((mask >> last_idx) & 1) or dp[mask][last_idx] == 0:
                    continue

                # Try to extend the current permutation by adding a new element.
                for next_idx in range(n):
                    # If nums[next_idx] is not yet in the current mask:
                    if not ((mask >> next_idx) & 1):
                        # Check the divisibility condition between the last element and the new element.
                        if nums[last_idx] % nums[next_idx] == 0 or nums[next_idx] % nums[last_idx] == 0:
                            # Form the new mask by including nums[next_idx].
                            new_mask = mask | (1 << next_idx)
                            # Add the count of permutations ending at nums[last_idx] to the new state.
                            dp[new_mask][next_idx] = (dp[new_mask][next_idx] + dp[mask][last_idx]) % MOD

        # The total number of special permutations is the sum of all permutations
        # that use all elements (represented by the full_mask) and end with any element.
        total_special_permutations = 0
        full_mask = (1 << n) - 1 # This mask has all 'n' bits set.
        for i in range(n):
            total_special_permutations = (total_special_permutations + dp[full_mask][i]) % MOD

        return total_special_permutations

```