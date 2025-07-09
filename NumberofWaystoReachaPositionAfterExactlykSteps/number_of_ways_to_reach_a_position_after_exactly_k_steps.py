class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7

        diff = endPos - startPos
        abs_diff = abs(diff)

        if abs_diff > k:
            return 0
        
        if (k - abs_diff) % 2 != 0:
            return 0
        
        num_right_steps = (k + diff) // 2

        fact = [1] * (k + 1)
        invFact = [1] * (k + 1)

        for i in range(1, k + 1):
            fact[i] = (fact[i-1] * i) % MOD
        
        invFact[k] = pow(fact[k], MOD - 2, MOD) 

        for i in range(k - 1, -1, -1):
            invFact[i] = (invFact[i+1] * (i+1)) % MOD

        n = k
        r = num_right_steps

        if r < 0 or r > n:
            return 0 

        numerator = fact[n]
        denominator_inv = (invFact[r] * invFact[n - r]) % MOD

        ans = (numerator * denominator_inv) % MOD
        return ans