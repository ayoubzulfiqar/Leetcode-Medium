class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        
        all_distinct_factors = set()

        def get_prime_factors(n: int) -> set[int]:
            factors = set()
            d = 2
            temp_n = n
            while d * d <= temp_n:
                if temp_n % d == 0:
                    factors.add(d)
                    while temp_n % d == 0:
                        temp_n //= d
                d += 1
            if temp_n > 1:
                factors.add(temp_n)
            return factors

        for num in nums:
            factors_of_num = get_prime_factors(num)
            all_distinct_factors.update(factors_of_num)
        
        return len(all_distinct_factors)