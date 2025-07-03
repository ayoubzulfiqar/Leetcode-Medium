import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for x, y in points:
            dist_sq = x*x + y*y
            if len(heap) < k:
                heapq.heappush(heap, (-dist_sq, [x, y]))
            else:
                if -dist_sq > heap[0][0]:
                    heapq.heapreplace(heap, (-dist_sq, [x, y]))
        result = []
        while heap:
            neg_dist_sq, point = heapq.heappop(heap)
            result.append(point)
        return result