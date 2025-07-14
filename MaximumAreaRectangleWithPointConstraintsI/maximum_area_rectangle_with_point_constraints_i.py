import itertools

class Solution:
    def maxAreaRectangle(self, points: list[list[int]]) -> int:
        n = len(points)
        max_area = -1

        # Convert points to tuples for easier set operations and consistency
        # This avoids issues with list comparisons in sets and allows for faster lookups.
        point_tuples = [tuple(p) for p in points]

        # Iterate through all unique combinations of 4 distinct points
        # The number of points is small (<= 10), so C(N, 4) is feasible.
        for combo_indices in itertools.combinations(range(n), 4):
            # Get the four points for the current combination
            p1 = point_tuples[combo_indices[0]]
            p2 = point_tuples[combo_indices[1]]
            p3 = point_tuples[combo_indices[2]]
            p4 = point_tuples[combo_indices[3]]

            # Extract x and y coordinates from these four points
            xs = sorted(list(set([p1[0], p2[0], p3[0], p4[0]])))
            ys = sorted(list(set([p1[1], p2[1], p3[1], p4[1]])))

            # A valid axis-parallel rectangle must have exactly two distinct x-coordinates
            # and exactly two distinct y-coordinates.
            if len(xs) == 2 and len(ys) == 2:
                x_min, x_max = xs[0], xs[1]
                y_min, y_max = ys[0], ys[1]

                # Ensure the rectangle is non-degenerate (i.e., has positive area)
                # This check is implicitly covered by len(xs)==2 and len(ys)==2 if coordinates are unique,
                # but explicitly states the requirement for positive area.
                if x_min == x_max or y_min == y_max:
                    continue # Skip if it's a line or a point (area 0)

                # The four chosen points must exactly match the four corners formed by (x_min, y_min), etc.
                required_corners = {
                    (x_min, y_min), (x_min, y_max),
                    (x_max, y_min), (x_max, y_max)
                }
                given_corners = {p1, p2, p3, p4}

                if required_corners == given_corners:
                    current_area = (x_max - x_min) * (y_max - y_min)

                    # Now, check the crucial constraint: no other point inside or on its border.
                    is_valid_rectangle = True
                    for i in range(n):
                        other_p = point_tuples[i]
                        # Skip the four points that form the current rectangle's corners
                        if other_p in given_corners:
                            continue

                        ox, oy = other_p[0], other_p[1]
                        # Check if the 'other_p' lies within or on the border of the current rectangle
                        if x_min <= ox <= x_max and y_min <= oy <= y_max:
                            is_valid_rectangle = False
                            break # Found an invalid point, this rectangle is not valid

                    # If no other point was found inside or on the border, update the maximum area
                    if is_valid_rectangle:
                        max_area = max(max_area, current_area)

        return max_area