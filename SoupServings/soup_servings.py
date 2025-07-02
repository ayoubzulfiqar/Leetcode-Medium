class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1.0

        N = (n + 24) // 25

        memo = {}

        def dp(a_units: int, b_units: int) -> float:
            if a_units <= 0 and b_units <= 0:
                return 0.5
            if a_units <= 0:
                return 1.0
            if b_units <= 0:
                return 0.0

            if (a_units, b_units) in memo:
                return memo[(a_units, b_units)]

            res = 0.25 * (
                dp(a_units - 4, b_units) +
                dp(a_units - 3, b_units - 1) +
                dp(a_units - 2, b_units - 2) +
                dp(a_units - 1, b_units - 3)
            )

            memo[(a_units, b_units)] = res
            return res

        return dp(N, N)