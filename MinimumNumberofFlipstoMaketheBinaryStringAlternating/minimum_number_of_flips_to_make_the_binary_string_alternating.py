class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        
        s_extended = s + s
        len_extended = 2 * n
        
        diff_0 = [0] * len_extended
        diff_1 = [0] * len_extended
        
        for j in range(len_extended):
            # Target char for pattern '0101...' (0 at even indices, 1 at odd)
            target_char_0 = '0' if j % 2 == 0 else '1'
            if s_extended[j] != target_char_0:
                diff_0[j] = 1
            
            # Target char for pattern '1010...' (1 at even indices, 0 at odd)
            target_char_1 = '1' if j % 2 == 0 else '0'
            if s_extended[j] != target_char_1:
                diff_1[j] = 1
                
        current_flips_0 = 0
        current_flips_1 = 0
        
        # Calculate initial flips for the first window (s[0:n])
        for k in range(n):
            current_flips_0 += diff_0[k]
            current_flips_1 += diff_1[k]
        
        min_flips_overall = min(current_flips_0, current_flips_1)
        
        # Slide the window across s_extended
        # The window starts at index i and has length n, so it covers s_extended[i : i+n]
        for i in range(1, n):
            # Remove the cost of the character leaving the window from the left
            current_flips_0 -= diff_0[i-1]
            current_flips_1 -= diff_1[i-1]
            
            # Add the cost of the new character entering the window from the right
            current_flips_0 += diff_0[i+n-1]
            current_flips_1 += diff_1[i+n-1]
            
            min_flips_overall = min(min_flips_overall, current_flips_0, current_flips_1)
            
        return min_flips_overall

```