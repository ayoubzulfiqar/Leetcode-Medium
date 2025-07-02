import math

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda p: p[1])

        arrows = 0
        current_end = -math.inf 

        for xstart, xend in points:
            if xstart > current_end:
                arrows += 1
                current_end = xend
            
        return arrows