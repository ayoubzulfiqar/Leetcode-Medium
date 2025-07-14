import math

class Solution:
    def countNonSpecialNumbers(self, l: int, r: int) -> int:
        # A number x is special if it has exactly 2 proper divisors.
        # Proper divisors are all positive divisors of x except x itself.
        #
        # A number has exactly 2 proper divisors if and only if it is the square of a prime number.
        # For example, if x = p^2 (where p is a prime), its divisors are 1, p, p^2.
        # Its proper divisors are 1 and p, which are exactly two.
        #
        # The problem asks for the count of numbers in the range [l, r] that are NOT special.
        # This can be calculated as: (total numbers in range) - (count of special numbers in range).
        # Total numbers in range = r - l + 1.

        # Determine the maximum prime number 'p' such that p*p could be within the range [l, r].
        # Since p*p <= r, p <= sqrt(r).
        # The maximum value of r is 10^9, so max_prime_candidate will be at most sqrt(10^9) approx 31622.
        max_prime_candidate = int(math.sqrt(r))

        # Use Sieve of Eratosthenes to find all prime numbers up to max_prime_candidate.
        # Initialize a boolean list where is_prime[i] is True if i is potentially prime.
        is_prime = [True] * (max_prime_candidate + 1)

        # 0 and 1 are not prime numbers.
        if max_prime_candidate >= 0:
            is_prime[0] = False
        if max_prime_candidate >= 1:
            is_prime[1] = False

        # Iterate from 2 up to sqrt(max_prime_candidate).
        # If a number 'p' is prime, mark all its multiples as not prime.
        for p in range(2, int(math.sqrt(max_prime_candidate)) + 1):
            if is_prime[p]:
                # Start marking multiples from p*p, as smaller multiples would have been marked by smaller primes.
                for multiple in range(p * p, max_prime_candidate + 1, p):
                    is_prime[multiple] = False

        # Count how many special numbers (squares of primes) fall within the range [l, r].
        special_count = 0
        # Iterate through all numbers from 2 up to max_prime_candidate.
        # If a number 'p' is prime (according to our sieve), check its square.
        for p in range(2, max_prime_candidate + 1):
            if is_prime[p]:
                p_squared = p * p
                # Check if p_squared is within the given range [l, r].
                # We need to ensure p_squared does not exceed r, as p could be max_prime_candidate.
                # The condition `p_squared <= r` is implicitly handled by `p <= max_prime_candidate = int(math.sqrt(r))`.
                # If p_squared is less than l, it's not in the range.
                if p_squared >= l:
                    special_count += 1
                # Optimization: if p_squared exceeds r, further p*p will also exceed r.
                # However, the loop for p already stops at max_prime_candidate where max_prime_candidate^2 <= r.
                # So p_squared will always be <= r. We only need to check p_squared >= l.

        # Calculate the total count of numbers in the range [l, r].
        total_numbers_in_range = r - l + 1

        # The result is the total numbers minus the special numbers.
        return total_numbers_in_range - special_count