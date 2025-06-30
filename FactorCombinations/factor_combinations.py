class Solution:
    def getFactors(self, n: int) -> list[list[int]]:
        results = []

        # Factors must be greater than 1 and less than n.
        # Numbers less than 4 (1, 2, 3) cannot have factor combinations
        # that satisfy the "factors greater than 1 and less than n" condition.
        if n < 4:
            return []

        def _dfs(remaining_num, start_divisor, current_factors):
            # Base case / When to add a combination:
            # If current_factors is not empty, it means we have found at least one
            # factor for the original 'n' before this point.
            # The 'remaining_num' itself is the last factor in this combination.
            # We append a copy of current_factors