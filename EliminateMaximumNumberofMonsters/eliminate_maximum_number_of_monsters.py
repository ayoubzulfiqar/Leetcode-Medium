class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        n = len(dist)
        
        times_to_reach = []
        for i in range(n):
            times_to_reach.append(dist[i] / speed[i])
            
        times_to_reach.sort()
        
        eliminated_count = 0
        current_time_elapsed = 0
        
        for t in times_to_reach:
            if t <= current_time_elapsed:
                return eliminated_count
            else:
                eliminated_count += 1
                current_time_elapsed += 1
                
        return eliminated_count