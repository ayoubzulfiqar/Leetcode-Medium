class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        results = []
        current_combination = []

        def backtrack(start_num):
            if len(current_combination) == k:
                results.append(list(current_combination))
                return

            # Optimization: Pruning
            # The maximum number we can pick for the current slot `i`
            # is `n - (k - len(current_combination)) + 1`.
            # This ensures that there are enough remaining numbers (from `i` to `n`)
            # to complete a combination of `k` elements.
            # `k - len(current_combination)` is the number of elements still needed.
            # `n - i + 1` is the count of available numbers from `i` to `n`.
            # We need `n - i + 1 >= k - len(current_combination)`.
            # Rearranging for `i`: `i <= n - (k - len(current_combination)) + 1`.
            # The loop range needs to include this upper bound, so we add 1.
            upper_bound = n - (k - len(current_combination)) + 1

            for i in range(start_num, upper_bound + 1):
                current_combination.append(i)
                backtrack(i + 1)
                current_combination.pop()

        backtrack(1)
        return results