class Solution:
    def hashDividedString(self, s: str, k: int) -> str:
        n = len(s)
        result_chars = []

        for i in range(0, n, k):
            substring = s[i : i + k]
            current_sum = 0
            for char_code in substring:
                current_sum += (ord(char_code) - ord('a'))
            
            hashed_char_value = current_sum % 26
            result_chars.append(chr(ord('a') + hashed_char_value))
            
        return "".join(result_chars)