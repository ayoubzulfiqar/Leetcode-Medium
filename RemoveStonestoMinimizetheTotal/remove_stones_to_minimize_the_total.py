import heapq

class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        max_heap = []
        for p in piles:
            heapq.heappush(max_heap, -p)
        
        for _ in range(k):
            current_pile = -heapq.heappop(max_heap)
            
            stones_removed = current_pile // 2
            
            new_pile = current_pile - stones_removed
            
            heapq.heappush(max_heap, -new_pile)
            
        total_stones = 0
        for p_neg in max_heap:
            total_stones += -p_neg
            
        return total_stones