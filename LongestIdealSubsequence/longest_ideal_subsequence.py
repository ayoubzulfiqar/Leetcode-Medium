class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26

        for char_s in s:
            current_char_val = ord(char_s) - ord('a')
            
            current_max_len_for_char = 0

            start_prev_char_val = max(0, current_char_val - k)
            end_prev_char_val = min(25, current_char_val + k)

            for prev_char_val in range(start_prev_char_val, end_prev_char_val + 1):
                current_max_len_for_char = max(current_max_len_for_char, dp[prev_char_val])
            
            dp[current_char_val] = current_max_len_for_char + 1
        
        return max(dp)