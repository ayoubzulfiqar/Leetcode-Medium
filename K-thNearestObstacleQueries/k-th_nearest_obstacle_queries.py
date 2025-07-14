import heapq

class Solution:
    def kthNearestObstacle(self, queries: list[list[int]], k: int) -> list[int]:
        results = []
        max_heap = [] 
        num_obstacles = 0

        for x, y in queries:
            distance = abs(x) + abs(y)
            num_obstacles += 1

            if len(max_heap) < k:
                heapq.heappush(max_heap, -distance)
            else:
                if distance < -max_heap[0]:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, -distance)
            
            if num_obstacles < k:
                results.append(-1)
            else:
                results.append(-max_heap[0])

        return results