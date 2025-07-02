import collections

class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        points = [p1, p2, p3, p4]
        
        def dist_sq(point_a, point_b):
            return (point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2

        squared_distances = []
        for i in range(4):
            for j in range(i + 1, 4):
                squared_distances.append(dist_sq(points[i], points[j]))
        
        counts = collections.Counter(squared_distances)
        
        if len(counts) != 2:
            return False
        
        sorted_items = sorted(counts.items())
        
        side_sq, side_count = sorted_items[0]
        diag_sq, diag_count = sorted_items[1]
        
        if side_sq == 0:
            return False
        
        if side_count != 4:
            return False
            
        if diag_count != 2:
            return False
            
        if 2 * side_sq != diag_sq:
            return False
            
        return True