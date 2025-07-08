class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        num_even_indices = (n + 1) // 2
        num_odd_indices = n // 2

        res_even_pos = pow(5, num_even_indices, MOD)
        res_odd_pos = pow(4, num_odd_indices, MOD)

        return (res_even_pos * res_odd_pos) % MOD