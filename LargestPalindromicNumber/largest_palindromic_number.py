import collections

class Solution:
    def largestPalindromic(self, num: str) -> str:
        counts = collections.Counter(num)
        
        left_half_chars = []
        middle_digit = ""
        
        for digit_char in "9876543210":
            count = counts[digit_char]
            
            left_half_chars.extend([digit_char] * (count // 2))
            
            if count % 2 == 1 and middle_digit == "":
                middle_digit = digit_char
        
        left_str = "".join(left_half_chars)
        
        if left_str and left_str[0] == '0':
            return middle_digit if middle_digit else "0"
            
        right_str = left_str[::-1]
        
        return left_str + middle_digit + right_str