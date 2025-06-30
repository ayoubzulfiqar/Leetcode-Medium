class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        areaA = (ax2 - ax1) * (ay2 - ay1)
        areaB = (bx2 - bx1) * (by2 - by1)

        intersect_x1 = max(ax1, bx1)
        intersect_y1 = max(ay1, by1)
        intersect_x2 = min(ax2, bx2)
        intersect_y2 = min(ay2, by2)

        intersect_width = max(0, intersect_x2 - intersect_x1)
        intersect_height = max(0, intersect_y2 - intersect_y1)

        areaIntersection = intersect_width * intersect_height

        totalArea = areaA + areaB - areaIntersection

        return totalArea