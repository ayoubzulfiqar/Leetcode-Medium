import math

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        
        # Iterate for factors up to sqrt(n)
        # These factors are found in ascending order
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                count += 1
                if count == k:
                    return i
        
        # If we reach here, k is greater than the number of factors <= sqrt(n).
        # Now we need to consider factors > sqrt(n). These are n // i.
        # We iterate i downwards from int(sqrt(n)) - 1 (or int(sqrt(n)) if n is not a perfect square).
        
        start_i = int(math.sqrt(n))
        
        # If n is a perfect square, the factor sqrt(n) (which is start_i) was already counted in the first loop
        # as 'i'. Its pair 'n // start_i' would also be start_i.
        # To avoid double-counting and to correctly get the next distinct factor,
        # we adjust the starting point for the reverse iteration.
        if start_i * start_i == n:
            start_i -= 1 
        
        # Iterate downwards for the larger factors (n // i)
        # These factors, when derived from decreasing 'i', will be found in ascending order.
        for i in range(start_i, 0, -1): 
            if n % i == 0:
                count += 1
                if count == k:
                    return n // i # This is the corresponding larger factor
        
        # If we finish all iterations and haven't returned, it means n has less than k factors.
        return -1