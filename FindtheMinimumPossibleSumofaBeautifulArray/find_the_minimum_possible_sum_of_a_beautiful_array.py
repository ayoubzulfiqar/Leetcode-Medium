class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        MOD = 10**9 + 7
        
        inv2 = pow(2, MOD - 2, MOD)
        
        count_small = min(n, target // 2)
        
        sum_small = (count_small % MOD * ((count_small + 1) % MOD)) % MOD
        sum_small = (sum_small * inv2) % MOD
        
        remaining_n = n - count_small
        
        sum_large = 0
        if remaining_n > 0:
            first_large = target
            last_large = target + remaining_n - 1
            
            sum_large = (remaining_n % MOD * ((first_large + last_large) % MOD)) % MOD
            sum_large = (sum_large * inv2) % MOD
            
        total_sum = (sum_small + sum_large) % MOD
        
        return total_sum