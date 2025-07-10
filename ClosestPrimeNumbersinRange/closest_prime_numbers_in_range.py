class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        max_val = right
        is_prime = [True] * (max_val + 1)
        if max_val >= 0:
            is_prime[0] = False
        if max_val >= 1:
            is_prime[1] = False

        for p in range(2, int(max_val**0.5) + 1):
            if is_prime[p]:
                for multiple in range(p * p, max_val + 1, p):
                    is_prime[multiple] = False

        primes_in_range = []
        for i in range(left, right + 1):
            if is_prime[i]:
                primes_in_range.append(i)

        if len(primes_in_range) < 2:
            return [-1, -1]

        min_diff = float('inf')
        result = [-1, -1]

        for i in range(len(primes_in_range) - 1):
            num1 = primes_in_range[i]
            num2 = primes_in_range[i+1]
            current_diff = num2 - num1

            if current_diff < min_diff:
                min_diff = current_diff
                result = [num1, num2]

        return result