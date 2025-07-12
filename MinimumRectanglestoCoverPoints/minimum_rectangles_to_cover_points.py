class Solution:
    def minRectanglesToCoverPoints(self, points: list[list[int]], w: int) -> int:
        points.sort(key=lambda p: p[0])

        rectangles_count = 0
        i = 0

        while i < len(points):
            rectangles_count += 1
            
            x_start = points[i][0]
            x_end_limit = x_start + w
            
            while i < len(points) and points[i][0] <= x_end_limit:
                i += 1
                
        return rectangles_count