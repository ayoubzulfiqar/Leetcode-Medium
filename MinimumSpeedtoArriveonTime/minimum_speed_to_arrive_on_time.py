import math

class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        n = len(dist)

        def check(speed: int) -> bool:
            total_time = 0.0
            for i in range(n - 1):
                total_time += math.ceil(dist[i] / speed)
            
            total_time += dist[n - 1] / speed
            
            return total_time <= hour

        low = 1
        high = 10**7 + 7 
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans