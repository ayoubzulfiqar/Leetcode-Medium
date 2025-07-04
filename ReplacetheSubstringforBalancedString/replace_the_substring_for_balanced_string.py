import collections

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        k = n // 4

        counts = collections.Counter(s)

        excess = {}
        for char in 'QWER':
            if counts[char] > k:
                excess[char] = counts[char] - k
        
        if not excess:
            return 0

        left = 0
        min_len = n 
        
        current_window_counts = collections.defaultdict(int)
        
        satisfied_excess_chars = 0 

        for right in range(n):
            char_right = s[right]
            current_window_counts[char_right] += 1

            if char_right in excess and current_window_counts[char_right] == excess[char_right]:
                satisfied_excess_chars += 1
            
            while satisfied_excess_chars == len(excess):
                min_len = min(min_len, right - left + 1)

                char_left = s[left]
                current_window_counts[char_left] -= 1

                if char_left in excess and current_window_counts[char_left] < excess[char_left]:
                    satisfied_excess_chars -= 1
                
                left += 1
        
        return min_len