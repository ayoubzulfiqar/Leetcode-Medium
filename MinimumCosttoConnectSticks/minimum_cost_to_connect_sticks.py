import heapq

class Solution:
    def connectSticks(self, sticks: list[int]) -> int:
        heapq.heapify(sticks)
        
        total_cost = 0
        
        while len(sticks) > 1:
            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)
            
            current_connection_cost = stick1 + stick2
            total_cost += current_connection_cost
            
            heapq.heappush(sticks, current_connection_cost)
            
        return total_cost