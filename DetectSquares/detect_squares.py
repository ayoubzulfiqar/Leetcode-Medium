```python
from collections import defaultdict

class DetectSquares:

    def __init__(self):
        # self.points stores the count of each point (x, y)
        # The key is a tuple (x, y) and the value is its frequency.
        self.points = defaultdict(int)

    def add(self, point: list[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: list[int]) -> int:
        x4, y4 = point
        total_squares = 0

        # Iterate through all unique points (x1, y1) that have been added.
        # These points will serve as the point diagonally opposite to the query point (x4, y4).
        for (x1, y1), count1 in self.points.items():
            # For (x1, y1) and (x4, y4) to be diagonally opposite corners of an axis-aligned square:
            # 1. They must not share the same x-coordinate (x1 != x4).
            # 2. They must not share the same y-coordinate (y1 != y4).
            # If they share an x or y coordinate, they cannot be diagonal corners of an axis-aligned square with positive area.
            if x1 == x4 or y1 == y4:
                continue

            # 3. The absolute difference in their x-coordinates must be equal to the absolute difference in their y-coordinates.
            # This ensures that the side lengths of the potential square are equal.
            side_length = abs(x1 - x4)
            if abs(y1 - y4) != side_length:
                continue

            # If all conditions above are met, (x1, y1) and (x4, y4) form a diagonal.
            # The other two required corners of the square would be:
            # P2 = (x1, y4)
            # P3 = (x4, y1)

            # Get the counts of these two required points from our data structure.
            # If a point does not exist, defaultdict will return 0, correctly making its contribution 0.
            count2 = self.points[(x1, y4)]
            count3 = self.points[(x4, y1)]

            # The number of ways to form this specific square is the product of the counts
            # of the three points chosen from the data structure (P1, P2, P3).
            # (P4 is the query point, not chosen from the data structure).
            total_squares += count1 * count2 * count3

        return total_squares

```