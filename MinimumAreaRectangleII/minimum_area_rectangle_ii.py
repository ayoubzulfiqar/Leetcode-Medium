import math

class Solution:
    def minAreaRect(self, points: list[list[int]]) -> float:
        n = len(points)
        if n < 4:
            return 0.0

        # Convert points to a set of tuples for O(1) lookup
        point_set = set()
        for p in points:
            point_set.add(tuple(p))

        min_area = float('inf')

        # Iterate over all unique combinations of three points (p1, p2, p3)
        # p1 will be the vertex where the right angle is formed.
        # p1p2 and p1p3 will be the two perpendicular sides.
        for i in range(n):
            p1 = points[i]
            x1, y1 = p1[0], p1[1]

            for j in range(n):
                if i == j: # Ensure p1 and p2 are distinct
                    continue
                p2 = points[j]
                x2, y2 = p2[0], p2[1]

                # Vector p1p2
                vec1_x, vec1_y = x2 - x1, y2 - y1
                
                for k in range(n):
                    if i == k or j == k: # Ensure p1, p2, and p3 are distinct
                        continue
                    p3 = points[k]
                    x3, y3 = p3[0], p3[1]

                    # Vector p1p3
                    vec2_x, vec2_y = x3 - x1, y3 - y1

                    # Check for perpendicularity: dot product of p1p2 and p1p3 must be zero
                    # (x2-x1)*(x3-x1) + (y2-y1)*(y3-y1) == 0
                    if vec1_x * vec2_x + vec1_y * vec2_y == 0:
                        # If perpendicular, p1, p2, p3 are three vertices of a potential rectangle
                        # with a right angle at p1.
                        
                        # The fourth vertex p4 can be found by vector addition: p4 = p2 + (p3 - p1)
                        # This is equivalent to (x4 - x2) = (x3 - x1) and (y4 - y2) = (y3 - y1)
                        # So, x4 = x2 + x3 - x1
                        # And, y4 = y2 + y3 - y1
                        p4_x, p4_y = x2 + x3 - x1, y2 + y3 - y1

                        # Check if the calculated fourth point exists in the input set
                        if (p4_x, p4_y) in point_set:
                            # We found a rectangle formed by p1, p2, (p4), p3.
                            # The sides of this rectangle are p1p2 and p1p3.
                            
                            # Calculate the squared lengths of these two perpendicular sides.
                            len_sq_p1p2 = vec1_x**2 + vec1_y**2
                            len_sq_p1p3 = vec2_x**2 + vec2_y**2
                            
                            # The area of the rectangle is the product of the lengths of its adjacent sides.
                            current_area = math.sqrt(len_sq_p1p2) * math.sqrt(len_sq_p1p3)
                            
                            # Update the minimum area found so far
                            min_area = min(min_area, current_area)

        # If min_area is still infinity, it means no rectangle was found.
        # In that case, return 0.0. Otherwise, return the minimum area found.
        return min_area if min_area != float('inf') else 0.0