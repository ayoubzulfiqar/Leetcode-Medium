class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count_zeros = 0
        for char_s in s:
            if char_s == '0':
                count_zeros += 1
        
        ans_length = count_zeros
        current_val = 0
        power = 1 # Represents 2^0, 2^1, 2^2, ...
        
        # Iterate from right to left (least significant bit to most significant bit)
        # to greedily add '1's while keeping the value small.
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                # Check if adding this '1' would exceed k
                if current_val + power <= k:
                    current_val += power
                    ans_length += 1
                else:
                    # If adding this '1' makes the number too large,
                    # then any '1's to its left (more significant) would also
                    # make the number too large. So, we cannot add any more '1's.
                    # We have already accounted for all possible '0's.
                    break
            
            # Update power for the next bit position (to the left)
            power *= 2
            
        return ans_length