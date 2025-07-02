class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        n = len(s)
        res_chars = list(s)
        
        current_shift_amount = 0 
        
        for i in range(n - 1, -1, -1):
            current_shift_amount = (current_shift_amount + shifts[i]) % 26
            
            original_char_pos = ord(s[i]) - ord('a')
            
            new_char_pos = (original_char_pos + current_shift_amount) % 26
            
            res_chars[i] = chr(new_char_pos + ord('a'))
            
        return "".join(res_chars)