class Solution:
    def numberOfWays(self, points: list[list[int]]) -> int:
        n = len(points)
        count = 0

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                x1, y1 = points[i]  # Point A
                x2, y2 = points[j]  # Point B

                # Condition 1: A is on the upper left side of B
                # This means x_A <= x_B and y_A >= y_B
                if not (x1 <= x2 and y1 >= y2):
                    continue

                # Define the rectangle boundaries based on A and B
                # The minimum x-coordinate is x1, maximum is x2
                # The minimum y-coordinate is y2, maximum is y1
                min_rect_x = x1
                max_rect_x = x2
                min_rect_y = y2
                max_rect_y = y1

                is_valid_pair = True
                for k in range(n):
                    if k == i or k == j:
                        continue

                    xp, yp = points[k]  # Point P

                    # Condition 2: Check if P is inside or on the border of the rectangle
                    # A point (xp, yp) is inside or on the border if:
                    # min_rect_x <= xp <= max_rect_x AND min_rect_y <= yp <= max_rect_y
                    if min_rect_x <= xp <= max_rect_x and min_rect_y <= yp <= max_rect_y:
                        is_valid_pair = False
                        break  # Found an obstructing point, this pair (A, B) is invalid

                if is_valid_pair:
                    count += 1

        return count