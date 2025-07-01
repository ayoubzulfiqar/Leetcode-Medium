class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1

        pointers = [0] * len(primes)
        next_multiples = [p for p in primes]

        for i in range(1, n):
            min_val = min(next_multiples)
            
            ugly[i] = min_val

            for j in range(len(primes)):
                if next_multiples[j] == min_val:
                    pointers[j] += 1
                    next_multiples[j] = ugly[pointers[j]] * primes[j]
        
        return ugly[n-1]