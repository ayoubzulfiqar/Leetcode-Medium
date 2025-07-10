class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7

        # The array nums contains integers from 1 to 2^p - 1.
        # Total number of elements is N = 2^p - 1.

        # For any bit position k (from 0 to p-1),
        # the count of '1's across all numbers from 1 to 2^p - 1 is 2^(p-1).
        # The count of '0's across all numbers from 1 to 2^p - 1 is (2^p - 1) - 2^(p-1) = 2^(p-1) - 1.

        # To minimize the product, we want to make as many numbers as possible equal to 1.
        # A number is 1 (binary 0...01) if its 0-th bit is 1 and all other p-1 bits are 0.
        # To achieve this for K numbers:
        # We need K '1's for bit 0. Max available '1's for bit 0 is 2^(p-1).
        # We need K '0's for each of bits 1 to p-1. Max available '0's for each of these bits is 2^(p-1) - 1.
        # The limiting factor is the number of '0's available for bits 1 to p-1.
        # So, we can make at most 2^(p-1) - 1 numbers equal to 1.

        # Let M = 2^(p-1) - 1.
        # We create M numbers equal to 1.
        # Bits consumed for these M numbers:
        # - M '1's for bit 0. Remaining '1's for bit 0: 2^(p-1) - M = 1.
        # - M '0's for each of bits 1 to p-1. Remaining '0's for each of these bits: (2^(p-1) - 1) - M = 0.
        # This means all '0's for bits 1 to p-1 are used up.

        # Number of remaining elements: N - M = (2^p - 1) - (2^(p-1) - 1) = 2^p - 2^(p-1) = 2^(p-1).
        # For these 2^(p-1) remaining elements:
        # - For bits 1 to p-1: Since all '0's are used, these 2^(p-1) elements MUST have '1' at these positions.
        # - For bit 0: One '1' is remaining. This '1' must go to one of these elements. The other 2^(p-1) - 1 elements must have '0' at bit 0.

        # This leads to the following configuration for the remaining 2^(p-1) elements:
        # 1. One element will have '1' at bit 0 and '1's at all other p-1 bits. This makes it 11...11 (value 2^p - 1).
        # 2. The other (2^(p-1) - 1) elements will have '0' at bit 0 and '1's at all other p-1 bits. This makes them 11...10 (value 2^p - 2).

        # So, the final array configuration for minimum non-zero product is:
        # - (2^(p-1) - 1) copies of value 1.
        # - 1 copy of value (2^p - 1).
        # - (2^(p-1) - 1) copies of value (2^p - 2).

        # The product will be 1^(2^(p-1) - 1) * (2^p - 1) * (2^p - 2)^(2^(p-1) - 1).
        # This simplifies to (2^p - 1) * (2^p - 2)^(2^(p-1) - 1).

        # Calculate (2^p - 1) % MOD
        val1 = (pow(2, p, MOD) - 1 + MOD) % MOD

        # Calculate (2^p - 2) % MOD
        val2 = (pow(2, p, MOD) - 2 + MOD) % MOD

        # Calculate the exponent for val2: 2^(p-1) - 1.
        # This exponent is a regular integer, not modulo. Python handles large integers.
        exponent = pow(2, p - 1) - 1

        # Compute the final product modulo MOD
        # pow(base, exp, mod) is used for modular exponentiation.
        # Note: For p=1, exponent becomes 0. pow(0, 0, MOD) correctly returns 1 in Python.
        result = (val1 * pow(val2, exponent, MOD)) % MOD

        return result