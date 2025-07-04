class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        total_sum = 0
        
        for num in nums:
            divisors = []
            
            # Numbers less than 6 cannot have exactly four divisors.
            # Smallest numbers with 4 divisors are 6 (1,2,3,6) and 8 (1,2,4,8).
            if num < 6:
                continue

            # Iterate up to the square root of num to find divisors
            limit = int(num**0.5)
            for i in range(1, limit + 1):
                if num % i == 0:
                    divisors.append(i)
                    if i * i != num: # If i is not the square root, then num/i is another distinct divisor
                        divisors.append(num // i)
                
                # Optimization: If we already found more than 4 divisors, this number
                # cannot qualify, so we can stop processing it early.
                if len(divisors) > 4:
                    break
            
            # Check if exactly four divisors were found for the current number
            if len(divisors) == 4:
                total_sum += sum(divisors)
                
        return total_sum