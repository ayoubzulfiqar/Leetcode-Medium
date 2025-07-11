class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def combinations_2(N):
            if N < 2:
                return 0
            return N * (N - 1) // 2

        # Total ways to distribute n candies among 3 children without any upper limit (c_i >= 0)
        # This is equivalent to C(n + 3 - 1, 3 - 1) = C(n + 2, 2)
        ans = combinations_2(n + 2)

        # Apply inclusion-exclusion principle
        # Subtract cases where at least one child gets more than 'limit' candies.
        # If a child gets c_i >= limit + 1 candies, let c_i' = c_i - (limit + 1).
        # The equation becomes c_i' + c_j + c_k = n - (limit + 1).
        # Number of ways for one child to exceed limit is C(n - (limit + 1) + 2, 2) = C(n - limit + 1, 2).
        # There are 3 children, so we subtract 3 * C(n - limit + 1, 2).
        ans -= 3 * combinations_2(n - limit + 1)

        # Add back cases where at least two children get more than 'limit' candies.
        # If two children get c_i >= limit + 1 and c_j >= limit + 1,
        # The equation becomes c_i' + c_j' + c_k = n - 2 * (limit + 1).
        # Number of ways for two children to exceed limit is C(n - 2 * (limit + 1) + 2, 2) = C(n - 2 * limit, 2).
        # There are C(3, 2) = 3 pairs of children, so we add 3 * C(n - 2 * limit, 2).
        ans += 3 * combinations_2(n - 2 * limit)

        # Subtract cases where all three children get more than 'limit' candies.
        # If all three children get c_i, c_j, c_k >= limit + 1,
        # The equation becomes c_i' + c_j' + c_k' = n - 3 * (limit + 1).
        # Number of ways for three children to exceed limit is C(n - 3 * (limit + 1) + 2, 2) = C(n - 3 * limit - 1, 2).
        # There is C(3, 3) = 1 triplet of children, so we subtract 1 * C(n - 3 * limit - 1, 2).
        ans -= 1 * combinations_2(n - 3 * limit - 1)

        return ans