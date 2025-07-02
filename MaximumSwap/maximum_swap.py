class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)

        for i in range(n):
            max_digit_val = s[i]
            max_digit_idx = -1
            
            # Find the rightmost largest digit to the right of s[i]
            # Iterate from right to left (n-1 down to i+1)
            for j in range(n - 1, i, -1):
                if s[j] > max_digit_val:
                    max_digit_val = s[j]
                    max_digit_idx = j
            
            # If a larger digit was found to the right of s[i]
            # and it's strictly greater than s[i]
            if max_digit_idx != -1 and s[max_digit_idx] > s[i]:
                # Perform the swap
                s[i], s[max_digit_idx] = s[max_digit_idx], s[i]
                return int("".join(s))
        
        # If no swap was performed, the number is already the maximum possible
        return num