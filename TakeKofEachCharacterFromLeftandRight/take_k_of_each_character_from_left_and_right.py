import collections

class Solution:
    def minimumMinutes(self, s: str, k: int) -> int:
        n = len(s)

        total_counts = collections.Counter(s)

        if total_counts['a'] < k or total_counts['b'] < k or total_counts['c'] < k:
            return -1
        
        max_allowed_in_middle = {
            'a': total_counts['a'] - k,
            'b': total_counts['b'] - k,
            'c': total_counts['c'] - k
        }

        current_window_counts = collections.Counter()
        left = 0
        max_len_middle_subarray = 0

        for right in range(n):
            current_window_counts[s[right]] += 1

            while (current_window_counts['a'] > max_allowed_in_middle['a'] or
                   current_window_counts['b'] > max_allowed_in_middle['b'] or
                   current_window_counts['c'] > max_allowed_in_middle['c']):
                current_window_counts[s[left]] -= 1
                left += 1
            
            max_len_middle_subarray = max(max_len_middle_subarray, right - left + 1)
        
        return n - max_len_middle_subarray