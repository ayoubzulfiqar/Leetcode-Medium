class Solution:
    def numberOfGoodStrings(self, n: int) -> int:
        MOD = 10**9 + 7

        def power(base, exp):
            res = 1
            base %= MOD
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return res

        # Total strings of length n using 26 lowercase English characters
        total_strings = power(26, n)

        # Calculate terms for Inclusion-Exclusion Principle
        # A string is "bad" if it cannot be rearranged to contain "leet".
        # This means it's missing 'l', OR missing at least two 'e's (i.e., has 0 or 1 'e'), OR missing 't'.

        # P_l: strings without 'l' (characters from 25 other letters)
        P_l = power(25, n)
        
        # P_t: strings without 't' (characters from 25 other letters)
        P_t = power(25, n)
        
        # P_e: strings with 0 or 1 'e'
        # Case 1: 0 'e's (characters from 25 other letters excluding 'e') -> 25^n
        # Case 2: 1 'e' (choose 1 position for 'e' in n ways, fill n-1 positions with 25 other letters) -> n * 25^(n-1)
        term_n_times_25_n_minus_1 = (n * power(25, n - 1)) % MOD
        P_e = (power(25, n) + term_n_times_25_n_minus_1) % MOD

        # P_l_intersect_P_t: strings without 'l' and 't' (characters from 24 other letters)
        P_l_intersect_P_t = power(24, n)

        # P_l_intersect_P_e: strings without 'l' and with 0 or 1 'e'
        # Case 1: 0 'e's (chars from 24 other letters excluding 'l', 'e') -> 24^n
        # Case 2: 1 'e' (choose 1 position, fill n-1 positions with 24 other letters) -> n * 24^(n-1)
        term_n_times_24_n_minus_1 = (n * power(24, n - 1)) % MOD
        P_l_intersect_P_e = (power(24, n) + term_n_times_24_n_minus_1) % MOD
        
        # P_e_intersect_P_t: strings without 't' and with 0 or 1 'e' (symmetric to P_l_intersect_P_e)
        P_e_intersect_P_t = (power(24, n) + term_n_times_24_n_minus_1) % MOD

        # P_l_intersect_P_e_intersect_P_t: strings without 'l', 't' and with 0 or 1 'e'
        # Case 1: 0 'e's (chars from 23 other letters excluding 'l', 'e', 't') -> 23^n
        # Case 2: 1 'e' (choose 1 position, fill n-1 positions with 23 other letters) -> n * 23^(n-1)
        term_n_times_23_n_minus_1 = (n * power(23, n - 1)) % MOD
        P_l_intersect_P_e_intersect_P_t = (power(23, n) + term_n_times_23_n_minus_1) % MOD

        # Sum of individual properties
        sum_singles = (P_l + P_e + P_t) % MOD
        
        # Sum of pairwise intersections
        sum_doubles = (P_l_intersect_P_e + P_l_intersect_P_t + P_e_intersect_P_t) % MOD
        
        # Sum of triple intersection
        sum_triples = P_l_intersect_P_e_intersect_P_t

        # Number of "bad" strings using Inclusion-Exclusion
        # |P_l U P_e U P_t| = |P_l| + |P_e| + |P_t| - (|P_l intersect P_e| + |P_l intersect P_t| + |P_e intersect P_t|) + |P_l intersect P_e intersect P_t|
        bad_strings = (sum_singles - sum_doubles + sum_triples) % MOD
        
        # Ensure the result is non-negative after modulo operation
        bad_strings = (bad_strings + MOD) % MOD

        # Number of "good" strings = Total strings - Number of "bad" strings
        ans = (total_strings - bad_strings + MOD) % MOD

        return ans

```