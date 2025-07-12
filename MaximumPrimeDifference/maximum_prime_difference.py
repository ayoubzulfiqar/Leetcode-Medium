class Solution:
    def maxPrimeDifference(self, nums: list[int]) -> int:
        primes_up_to_100 = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

        first_prime_idx = -1
        last_prime_idx = -1

        for i in range(len(nums)):
            if nums[i] in primes_up_to_100:
                if first_prime_idx == -1:
                    first_prime_idx = i
                last_prime_idx = i
        
        return last_prime_idx - first_prime_idx