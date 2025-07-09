class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        
        diff_array = [0] * (n + 1)
        
        for start, end, direction in shifts:
            val = 1 if direction == 1 else -1
            diff_array[start] += val
            if end + 1 < n + 1:
                diff_array[end + 1] -= val
                
        net_shifts = [0] * n
        current_shift = 0
        for i in range(n):
            current_shift += diff_array[i]
            net_shifts[i] = current_shift
            
        result_chars = [''] * n
        for i in range(n):
            original_char_code = ord(s[i]) - ord('a')
            
            new_char_code = (original_char_code + net_shifts[i]) % 26
            
            result_chars[i] = chr(ord('a') + new_char_code)
            
        return "".join(result_chars)