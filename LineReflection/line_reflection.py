from typing import List

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if not points:
            return True

        min_x = float('inf')
        max_x = float('-inf')
        
        point_set = set()

        for p in points:
            x, y = p[0], p[1]
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            point_set.add((x, y))
        
        center_x = (min_x + max_x) / 2.0
        
        for x, y in point_set:
            reflected_x = 2 * center_x - x
            
            if (reflected_x, y) not in point_set:
                return False
                
        return True