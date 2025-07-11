class Solution:
    def largestSquareArea(self, bottomLeft: list[list[int]], topRight: list[list[int]]) -> int:
        n = len(bottomLeft)
        max_side_length = 0

        for i in range(n):
            for j in range(i + 1, n):
                # Rectangle i coordinates
                ax_i, by_i = bottomLeft[i]
                cx_i, dy_i = topRight[i]

                # Rectangle j coordinates
                ax_j, by_j = bottomLeft[j]
                cx_j, dy_j = topRight[j]

                # Calculate the bottom-left and top-right coordinates of the potential intersection rectangle
                # The x-coordinate of the intersection's bottom-left corner is the maximum of the two x-coordinates
                ix_bl = max(ax_i, ax_j)
                # The y-coordinate of the intersection's bottom-left corner is the maximum of the two y-coordinates
                iy_bl = max(by_i, by_j)

                # The x-coordinate of the intersection's top-right corner is the minimum of the two x-coordinates
                ix_tr = min(cx_i, cx_j)
                # The y-coordinate of the intersection's top-right corner is the minimum of the two y-coordinates
                iy_tr = min(dy_i, dy_j)

                # Check if a valid intersecting rectangle exists
                # An intersection exists if the calculated bottom-left is strictly less than the top-right
                # in both x and y dimensions. If ix_bl >= ix_tr or iy_bl >= iy_tr,
                # the rectangles do not overlap or only touch at a line/point, which cannot contain a square with positive area.
                if ix_bl < ix_tr and iy_bl < iy_tr:
                    # Calculate the width and height of the intersecting rectangle
                    intersection_width = ix_tr - ix_bl
                    intersection_height = iy_tr - iy_bl

                    # The largest square that can fit inside this intersecting rectangle
                    # will have a side length equal to the minimum of its width and height.
                    current_side_length = min(intersection_width, intersection_height)

                    # Update the maximum side length found across all pairs
                    max_side_length = max(max_side_length, current_side_length)

        # The final result is the area of the largest square, which is side_length * side_length
        return max_side_length * max_side_length

```