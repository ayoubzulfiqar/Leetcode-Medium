import bisect

class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.sort()

        min_overall_radius = 0

        for house_pos in houses:
            idx = bisect.bisect_left(heaters, house_pos)

            dist_to_right_heater = float('inf')
            dist_to_left_heater = float('inf')

            if idx < len(heaters):
                dist_to_right_heater = abs(house_pos - heaters[idx])
            
            if idx > 0:
                dist_to_left_heater = abs(house_pos - heaters[idx - 1])
            
            current_house_min_dist = min(dist_to_right_heater, dist_to_left_heater)
            
            min_overall_radius = max(min_overall_radius, current_house_min_dist)
        
        return min_overall_radius