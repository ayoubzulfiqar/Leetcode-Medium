import collections

class Solution:
    def countPairs(self, coordinates: list[list[int]], k: int) -> int:
        total_pairs = 0
        seen_points = collections.defaultdict(int)
        
        for x1, y1 in coordinates:
            for dx in range(k + 1):
                dy = k - dx
                
                x2_target = x1 ^ dx
                y2_target = y1 ^ dy
                
                if (x2_target, y2_target) in seen_points:
                    total_pairs += seen_points[(x2_target, y2_target)]
            
            seen_points[(x1, y1)] += 1
            
        return total_pairs