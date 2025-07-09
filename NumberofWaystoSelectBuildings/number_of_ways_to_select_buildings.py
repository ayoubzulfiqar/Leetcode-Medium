class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        
        total_zeros = s.count('0')
        total_ones = n - total_zeros
        
        ways = 0
        
        zeros_left = 0
        ones_left = 0
        
        for i in range(n):
            if s[i] == '0':
                # If the current building is '0', it can be the middle building
                # of a "101" pattern.
                # We need a '1' before it and a '1' after it.
                
                # Number of '1's to the left of the current index
                # is already stored in ones_left.
                
                # Number of '1's to the right of the current index:
                # total_ones (all '1's) - ones_left (ones before) - 0 (current is '0')
                ones_right = total_ones - ones_left
                
                ways += ones_left * ones_right
                
                # Update count of '0's seen so far for the next iteration
                zeros_left += 1
            else: # s[i] == '1'
                # If the current building is '1', it can be the middle building
                # of a "010" pattern.
                # We need a '0' before it and a '0' after it.
                
                # Number of '0's to the left of the current index
                # is already stored in zeros_left.
                
                # Number of '0's to the right of the current index:
                # total_zeros (all '0's) - zeros_left (zeros before) - 0 (current is '1')
                zeros_right = total_zeros - zeros_left
                
                ways += zeros_left * zeros_right
                
                # Update count of '1's seen so far for the next iteration
                ones_left += 1
                
        return ways