class Solution:
    def solve(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        max_val = n + k - 1
        
        fact = [1] * (max_val + 1)
        for i in range(1, max_val + 1):
            fact[i] = (fact[i-1] * i) % MOD
            
        invFact = [1] * (max_val + 1)
        invFact[max_val] = pow(fact[max_val], MOD - 2, MOD)
        for i in range(max_val - 1, -1, -1):
            invFact[i] = (invFact[i+1] * (i+1)) % MOD
            
        def nCr_mod_p(n_val, r_val):
            if r_val < 0 or r_val > n_val:
                return 0
            numerator = fact[n_val]
            denominator = (invFact[r_val] * invFact[n_val - r_val]) % MOD
            return (numerator * denominator) % MOD
            
        N_comb = k + n - 1
        K_comb = n - 1
        
        return nCr_mod_p(N_comb, K_comb)