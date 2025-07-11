class Solution:
    def getGoodIndices(self, variables: list[list[int]], target: int) -> list[int]:
        good_indices = []
        for i, var_set in enumerate(variables):
            a, b, c, m = var_set

            # Calculate (a^b) % 10
            # Using pow(base, exp, mod) for efficient modular exponentiation
            val1 = pow(a, b, 10)

            # Calculate (val1^c) % m
            final_val = pow(val1, c, m)

            # Check if the final result equals the target
            if final_val == target:
                good_indices.append(i)

        return good_indices