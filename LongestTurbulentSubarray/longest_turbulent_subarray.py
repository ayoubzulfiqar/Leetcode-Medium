class Solution:
    def longestTurbulentSubarray(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 1:
            return n

        max_len = 1
        # inc_len: length of current turbulent subarray ending with arr[i-1] < arr[i]
        inc_len = 1
        # dec_len: length of current turbulent subarray ending with arr[i-1] > arr[i]
        dec_len = 1

        for i in range(1, n):
            if arr[i] > arr[i-1]:
                # If arr[i] > arr[i-1], it can extend a 'dec' sequence (ending with >)
                # to form a 'dec > inc' pattern.
                inc_len = dec_len + 1
                # A 'dec' sequence cannot be extended, so it resets to 1 (current element only).
                dec_len = 1
            elif arr[i] < arr[i-1]:
                # If arr[i] < arr[i-1], it can extend an 'inc' sequence (ending with <)
                # to form an 'inc < dec' pattern.
                dec_len = inc_len + 1
                # An 'inc' sequence cannot be extended, so it resets to 1.
                inc_len = 1
            else:  # arr[i] == arr[i-1]
                # If elements are equal, both patterns are broken. Reset both lengths to 1.
                inc_len = 1
                dec_len = 1
            
            # Update the overall maximum length found so far.
            max_len = max(max_len, inc_len, dec_len)
        
        return max_len