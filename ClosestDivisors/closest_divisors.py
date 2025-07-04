import math

class Solution:
    def closestDivisors(self, num: int) -> list[int]:
        
        def find_best_pair(n: int) -> list[int]:
            # Iterate downwards from the integer part of sqrt(n)
            # The first divisor 'i' found will yield the pair (i, n/i)
            # that has the smallest absolute difference for the given 'n'.
            for i in range(int(math.sqrt(n)), 0, -1):
                if n % i == 0:
                    return [i, n // i]
            # This line should theoretically not be reached for n >= 1
            # as 1 is always a divisor.
            return [1, n] 

        # Calculate the two potential target numbers
        target1 = num + 1
        target2 = num + 2

        # Find the closest divisor pair for each target number
        pair1 = find_best_pair(target1)
        pair2 = find_best_pair(target2)

        # Calculate the absolute differences for each pair
        diff1 = abs(pair1[0] - pair1[1])
        diff2 = abs(pair2[0] - pair2[1])

        # Return the pair with the smaller absolute difference.
        # If differences are equal, prioritize the pair from num + 1.
        if diff1 <= diff2:
            return pair1
        else:
            return pair2