class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 0
        for i in range(1, n + 1):
            num_bits = i.bit_length()
            result = (result << num_bits) % MOD
            result = (result + i) % MOD
        return result