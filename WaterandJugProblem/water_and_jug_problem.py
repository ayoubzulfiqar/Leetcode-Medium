import math

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target == 0:
            return True
        
        if target > x + y:
            return False
            
        common_divisor = math.gcd(x, y)
        
        return target % common_divisor == 0