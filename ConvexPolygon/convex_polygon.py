class Solution:
    def isConvex(self, points: list[list[int]]) -> bool:
        n = len(points)
        if n < 3:
            return True
        
        expected_direction = 0 

        for i in range(n):
            p1 = points[i]
            p2 = points[(i + 1) % n]
            p3 = points[(i + 2) % n]
            
            cross_product_val = (p2[0] - p1[0]) * (p3[1] - p2[1]) - \
                                (p2[1] - p1[1]) * (p3[0] - p2[0])

            if cross_product_val != 0:
                current_direction = 1 if cross_product_val > 0 else -1
                
                if expected_direction == 0:
                    expected_direction = current_direction
                elif expected_direction != current_direction:
                    return False
        
        return True