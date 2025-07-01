class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        remainder = n % 3
        quotient = n // 3
        
        if remainder == 0:
            return 3**quotient
        elif remainder == 1:
            return (3**(quotient - 1)) * 4
        else: # remainder == 2
            return (3**quotient) * 2