import heapq

class Solution:
    def eatenApples(self, apples: list[int], days: list[int]) -> int:
        n = len(apples)
        eaten_apples = 0
        
        available_apples = [] 
        
        day = 0
        while day < n or available_apples:
            if day < n and apples[day] > 0:
                heapq.heappush(available_apples, (day + days[day], apples[day]))
            
            while available_apples and available_apples[0][0] <= day:
                heapq.heappop(available_apples)
                
            if available_apples:
                rotting_day, count = heapq.heappop(available_apples)
                eaten_apples += 1
                count -= 1
                if count > 0:
                    heapq.heappush(available_apples, (rotting_day, count))
            
            day += 1
            
        return eaten_apples