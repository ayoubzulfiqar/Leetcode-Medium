class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        
        total_ones = 0
        for char in s:
            if char == '1':
                total_ones += 1
        
        current_ones_in_prefix = 0
        
        min_flips = float('inf')
        
        for i in range(n + 1):
            # Calculate flips needed for the prefix s[0...i-1] to be all '0's
            # This is simply the count of '1's in s[0...i-1]
            flips_for_prefix_zeros = current_ones_in_prefix
            
            # Calculate flips needed for the suffix s[i...n-1] to be all '1's
            # First, find the count of '1's in the suffix
            ones_in_suffix = total_ones - current_ones_in_prefix
            
            # Then, find the count of '0's in the suffix
            # Length of suffix is (n - i)
            # Zeros in suffix = (Length of suffix) - (Ones in suffix)
            flips_for_suffix_ones = (n - i) - ones_in_suffix
            
            # Total flips for this split point
            current_total_flips = flips_for_prefix_zeros + flips_for_suffix_ones
            
            # Update the minimum flips found
            min_flips = min(min_flips, current_total_flips)
            
            # If not at the end of the string, update current_ones_in_prefix for the next iteration
            if i < n:
                if s[i] == '1':
                    current_ones_in_prefix += 1
        
        return min_flips