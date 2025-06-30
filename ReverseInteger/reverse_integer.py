class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1

        is_negative = x < 0
        num = abs(x)
        
        reversed_x = 0
        while num != 0:
            digit = num % 10
            reversed_x = reversed_x * 10 + digit
            num //= 10
        
        if is_negative:
            reversed_x = -reversed_x
        
        if not (MIN_INT <= reversed_x <= MAX_INT):
            return 0
        
        return reversed_x