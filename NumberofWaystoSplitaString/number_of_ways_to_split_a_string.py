class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        ones_indices = []
        for i, char in enumerate(s):
            if char == '1':
                ones_indices.append(i)

        total_ones = len(ones_indices)

        if total_ones % 3 != 0:
            return 0

        if total_ones == 0:
            # If all characters are '0', any split works as long as parts are non-empty.
            # We need to choose 2 split points from n-1 possible positions.
            # The number of ways to choose 2 items from n-1 is C(n-1, 2) = (n-1)*(n-2)/2
            return ((n - 1) * (n - 2) // 2) % MOD

        # If total_ones > 0 and is divisible by 3
        target_ones_per_part = total_ones // 3

        # Calculate the number of ways to make the first cut.
        # The first part (s1) must contain `target_ones_per_part` ones.
        # This means the cut must be placed after the `target_ones_per_part`-th '1'
        # and before the `(target_ones_per_part + 1)`-th '1'.
        # The `target_ones_per_part`-th '1' is at index `ones_indices[target_ones_per_part - 1]`.
        # The `(target_ones_per_part + 1)`-th '1' is at index `ones_indices[target_ones_per_part]`.
        # The number of valid positions for the first cut is the difference between these indices.
        ways1 = ones_indices[target_ones_per_part] - ones_indices[target_ones_per_part - 1]

        # Calculate the number of ways to make the second cut.
        # The first two parts (s1 + s2) must contain `2 * target_ones_per_part` ones.
        # This means the cut must be placed after the `(2 * target_ones_per_part)`-th '1'
        # and before the `(2 * target_ones_per_part + 1)`-th '1'.
        # The `(2 * target_ones_per_part)`-th '1' is at index `ones_indices[2 * target_ones_per_part - 1]`.
        # The `(2 * target_ones_per_part + 1)`-th '1' is at index `ones_indices[2 * target_ones_per_part]`.
        # The number of valid positions for the second cut is the difference between these indices.
        ways2 = ones_indices[2 * target_ones_per_part] - ones_indices[2 * target_ones_per_part - 1]

        # The total number of ways is the product of ways for the two independent cuts.
        return (ways1 * ways2) % MOD

```