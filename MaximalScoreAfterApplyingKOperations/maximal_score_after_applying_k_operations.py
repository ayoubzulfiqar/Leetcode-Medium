import heapq

class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
        
        total_score = 0
        
        for _ in range(k):
            current_max = -heapq.heappop(max_heap)
            
            total_score += current_max
            
            new_val = (current_max + 2) // 3
            
            heapq.heappush(max_heap, -new_val)
            
        return total_score