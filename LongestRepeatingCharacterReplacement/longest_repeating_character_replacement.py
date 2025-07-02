class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        
        freq_map = [0] * 26 
        
        max_freq = 0 
        
        for right in range(len(s)):
            char_code = ord(s[right]) - ord('A')
            freq_map[char_code] += 1
            
            max_freq = max(max_freq, freq_map[char_code])
            
            current_window_length = right - left + 1
            
            if current_window_length - max_freq > k:
                char_to_remove_code = ord(s[left]) - ord('A')
                freq_map[char_to_remove_code] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            
        return max_len