class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        n = len(s)
        num_substrings = 0
        current_idx = 0

        while current_idx < n:
            num_substrings += 1
            current_val = 0
            
            # j will be the potential end index of the current substring + 1
            j = current_idx
            while j < n:
                digit = int(s[j])
                
                # If this is the first digit of a new substring (current_val is 0)
                # and the digit itself is greater than k, then no valid partition exists.
                # Digits are guaranteed to be '1' through '9', so digit will always be >= 1.
                if current_val == 0 and digit > k:
                    return -1 
                
                # Calculate the value if we append the current digit.
                # Python handles large integers, so `current_val * 10 + digit`
                # will not overflow standard integer limits.
                potential_val = current_val * 10 + digit
                
                if potential_val <= k:
                    current_val = potential_val
                    j += 1 # Extend the current substring and move to the next character
                else:
                    # Cannot extend the current substring with s[j] as it would exceed k.
                    # The current substring ends at s[j-1].
                    break
            
            # After the inner loop, j points to the character where the next substring should start.
            # Update current_idx for the next iteration of the outer loop.
            current_idx = j
            
        return num_substrings