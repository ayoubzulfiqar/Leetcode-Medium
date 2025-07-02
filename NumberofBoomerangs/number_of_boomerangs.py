import collections

class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        total_boomerangs = 0
        
        for i in range(len(points)):
            point_i = points[i]
            
            distance_counts = collections.defaultdict(int)
            
            for j in range(len(points)):
                if i == j:
                    continue
                
                point_j = points[j]
                
                dx = point_i[0] - point_j[0]
                dy = point_i[1] - point_j[1]
                squared_distance = dx*dx + dy*dy
                
                distance_counts[squared_distance] += 1
            
            for count in distance_counts.values():
                if count >= 2:
                    total_boomerangs += count * (count - 1)
                    
        return total_boomerangs