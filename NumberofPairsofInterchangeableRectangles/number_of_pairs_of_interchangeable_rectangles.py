import math
from collections import defaultdict

class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        ratio_counts = defaultdict(int)
        
        for width, height in rectangles:
            common_divisor = math.gcd(width, height)
            
            simplified_width = width // common_divisor
            simplified_height = height // common_divisor
            
            ratio_counts[(simplified_width, simplified_height)] += 1
            
        total_pairs = 0
        for count in ratio_counts.values():
            if count >= 2:
                total_pairs += (count * (count - 1)) // 2
                
        return total_pairs