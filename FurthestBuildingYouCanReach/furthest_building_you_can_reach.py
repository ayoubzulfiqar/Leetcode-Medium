import heapq

class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        jumps_covered_by_bricks = [] 

        n = len(heights)
        for i in range(n - 1):
            diff = heights[i+1] - heights[i]

            if diff <= 0:
                continue
            
            heapq.heappush(jumps_covered_by_bricks, -diff)
            bricks -= diff

            if bricks < 0:
                if ladders > 0:
                    largest_jump_cost = -heapq.heappop(jumps_covered_by_bricks)
                    bricks += largest_jump_cost
                    ladders -= 1
                else:
                    return i
        
        return n - 1