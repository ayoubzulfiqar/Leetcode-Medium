import collections

class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        counts = collections.Counter(arr)
        
        # Sort keys by absolute value.
        # This ensures that for any pair (x, 2x), the number with the smaller
        # absolute value (which is 'x') is processed before the one with the
        # larger absolute value (which is '2x').
        # For example, -2 will be processed before -4, and 2 before 4.
        # If absolute values are equal (e.g., -2 and 2), their relative order
        # doesn't strictly matter for pairing as they won't be paired with each other.
        # Python's sorted is stable, so original order for equal keys is preserved.
        sorted_keys = sorted(counts.keys(), key=abs)
        
        for x in sorted_keys:
            # If all instances of x have already been paired, skip.
            if counts[x] == 0:
                continue
            
            # Handle the special case of zero
            if x == 0:
                # Zeros must be paired with other zeros.
                # If there's an odd number of zeros, they cannot all be paired.
                if counts[0] % 2 != 0:
                    return False
                # All zeros are accounted for, clear its count.
                counts[0] = 0
                continue 
            
            # Determine the required partner.
            # Based on the sorting strategy (by absolute value), 'x' will always be
            # the number that needs to find its double '2x'.
            # For example, if x = -2, we look for 2x = -4.
            # If x = 2, we look for 2x = 4.
            target = 2 * x
            
            # Check if there are enough 'target' values to pair with all 'x' values.
            # If not, it's impossible to form the required pairs.
            if counts[target] < counts[x]:
                return False
            
            # If there are enough, decrement the count of 'target' values.
            # All instances of 'x' are now considered paired.
            counts[target] -= counts[x]
            counts[x] = 0 # Mark x as fully processed
            
        # If the loop completes, it means all numbers have been successfully paired.
        return True