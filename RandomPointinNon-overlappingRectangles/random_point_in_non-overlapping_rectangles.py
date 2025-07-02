import random
import bisect

class Solution:

    def __init__(self, rects: list[list[int]]):
        self.rects = rects
        self.weights = []
        current_weight = 0
        for ai, bi, xi, yi in rects:
            width = xi - ai + 1
            height = yi - bi + 1
            points_in_rect = width * height
            current_weight += points_in_rect
            self.weights.append(current_weight)
        self.total_points = current_weight

    def pick(self) -> list[int]:
        target = random.randint(1, self.total_points)
        
        rect_idx = bisect.bisect_left(self.weights, target)
        
        ai, bi, xi, yi = self.rects[rect_idx]
        
        u = random.randint(ai, xi)
        v = random.randint(bi, yi)
        
        return [u, v]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()