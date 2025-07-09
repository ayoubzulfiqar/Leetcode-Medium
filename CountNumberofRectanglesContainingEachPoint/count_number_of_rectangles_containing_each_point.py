import bisect

class Solution:
    def countRectangles(self, rectangles: list[list[int]], points: list[list[int]]) -> list[int]:
        rects_by_height = [[] for _ in range(101)]

        for l, h in rectangles:
            rects_by_height[h].append(l)

        for h in range(1, 101):
            rects_by_height[h].sort()

        answer = [0] * len(points)

        for i, (xj, yj) in enumerate(points):
            count_for_point = 0
            for h in range(yj, 101):
                lengths_at_h = rects_by_height[h]
                
                idx = bisect.bisect_left(lengths_at_h, xj)
                
                count_for_point += len(lengths_at_h) - idx
            
            answer[i] = count_for_point
            
        return answer