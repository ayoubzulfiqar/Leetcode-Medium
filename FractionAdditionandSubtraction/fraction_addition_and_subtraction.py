import math
import re

class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a, b):
            return math.gcd(a, b)

        def lcm(a, b):
            return (a * b) // gcd(a, b)

        total_num = 0
        total_den = 1

        fractions = re.findall(r"([+-]?\d+/\d+)", expression)

        for frac_str in fractions:
            parts = frac_str.split('/')
            n = int(parts[0])
            d = int(parts[1])

            common_den = lcm(total_den, d)
            
            total_num = total_num * (common_den // total_den) + n * (common_den // d)
            total_den = common_den
        
        if total_num == 0:
            return "0/1"
        
        common_divisor = gcd(abs(total_num), total_den)
        
        total_num //= common_divisor
        total_den //= common_divisor
        
        return f"{total_num}/{total_den}"