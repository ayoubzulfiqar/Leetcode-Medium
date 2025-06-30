class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        sign = 1
        if i < n:
            if s[i] == '-':
                sign = -1
                i += 1
            elif s[i] == '+':
                i += 1

        result = 0
        
        abs_int_min_val = abs(INT_MIN)

        while i < n and s[i].isdigit():
            digit = int(s[i])

            if sign == 1:
                if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                    return INT_MAX
            else: 
                if result > abs_int_min_val // 10 or (result == abs_int_min_val // 10 and digit > abs_int_min_val % 10):
                    return INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        return result * sign