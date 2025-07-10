import math

class Solution:
    def minimumTime(self, ranks: list[int], cars: int) -> int:
        def check(time: int) -> bool:
            total_cars_repaired = 0
            for r in ranks:
                # A mechanic with rank r can repair n cars in r * n^2 minutes.
                # To find the maximum number of cars 'n' a mechanic can repair within 'time' minutes:
                # r * n^2 <= time
                # n^2 <= time / r
                # n <= sqrt(time / r)
                # Since 'n' must be an integer, we take the floor of sqrt(time / r).
                # Python's math.sqrt returns a float, and int() truncates (which is equivalent to floor for positive numbers).
                total_cars_repaired += int(math.sqrt(time / r))
            return total_cars_repaired >= cars

        # The minimum possible time is 1 (when a mechanic with rank 1 repairs 1 car).
        low = 1
        
        # The maximum possible time can be estimated.
        # In the worst case, one mechanic with the highest rank (100) repairs all cars (10^6).
        # Time = rank * cars^2 = 100 * (10^6)^2 = 100 * 10^12 = 10^14.
        # This value serves as a safe upper bound for our binary search.
        high = 100 * (10**6)**2 
        
        # Initialize the answer with the upper bound, as it's a guaranteed possible time.
        ans = high 

        # Perform binary search for the minimum time.
        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                # If 'mid' time is sufficient to repair all cars,
                # it could be our answer. We try to find an even smaller time.
                ans = mid
                high = mid - 1
            else:
                # If 'mid' time is not sufficient, we need more time.
                low = mid + 1

        return ans