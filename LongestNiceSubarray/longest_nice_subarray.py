class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        max_len = 0
        left = 0
        # bit_counts[j] stores the number of elements in the current window
        # that have the j-th bit set.
        # Max value of nums[i] is 10^9, which is less than 2^30.
        # So we need to check bits from 0 to 29.
        bit_counts = [0] * 30 
        
        # current_or_val stores the bitwise OR of all elements in the current window.
        # This is used to efficiently check for conflicts:
        # if (current_or_val & num) != 0, it means num shares at least one set bit
        # with some number already in the window.
        current_or_val = 0

        for right in range(len(nums)):
            num = nums[right]

            # While the current number 'num' conflicts with any number in the window
            # (i.e., they share a common set bit), shrink the window from the left.
            while (current_or_val & num) != 0:
                left_num = nums[left]
                # Remove left_num's contribution from bit_counts and current_or_val
                for j in range(30):
                    if (left_num >> j) & 1: # If j-th bit of left_num is set
                        bit_counts[j] -= 1
                        if bit_counts[j] == 0:
                            # If no other number in the window has this bit set,
                            # clear it from current_or_val.
                            current_or_val &= (~(1 << j))
                left += 1
            
            # After shrinking (if necessary), 'num' can now be added to the window.
            # Add num's contribution to bit_counts and current_or_val.
            for j in range(30):
                if (num >> j) & 1: # If j-th bit of num is set
                    bit_counts[j] += 1
            current_or_val |= num
            
            # Update the maximum length found so far.
            max_len = max(max_len, right - left + 1)
            
        return max_len

```