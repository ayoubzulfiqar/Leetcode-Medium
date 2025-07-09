class Solution:
    def powersOfTwo(self, n: int, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7

        powers = []
        current_power = 1
        # Iterate through bits of n to find powers of 2 that sum to n
        # n <= 10^9, which is less than 2^30. So, bits up to 29 are relevant.
        for i in range(31): 
            if (n >> i) & 1:
                powers.append(current_power)
            current_power *= 2

        # Calculate prefix products modulo MOD
        # prefix_products[k] will store the product of powers[0] * ... * powers[k-1]
        # prefix_products[0] is 1 (representing an empty product)
        prefix_products = [1] * (len(powers) + 1)
        for i in range(len(powers)):
            prefix_products[i+1] = (prefix_products[i] * powers[i]) % MOD

        answers = []
        for left, right in queries:
            # The product powers[left] * ... * powers[right] can be found by:
            # (product powers[0]...powers[right]) / (product powers[0]...powers[left-1])
            # This translates to (prefix_products[right+1]) / (prefix_products[left])
            # In modular arithmetic, division by X is multiplication by X^(MOD-2) (modular inverse)
            # using Fermat's Little Theorem, since MOD is a prime number.
            
            numerator = prefix_products[right+1]
            denominator_inverse = pow(prefix_products[left], MOD - 2, MOD)

            ans = (numerator * denominator_inverse) % MOD
            answers.append(ans)

        return answers