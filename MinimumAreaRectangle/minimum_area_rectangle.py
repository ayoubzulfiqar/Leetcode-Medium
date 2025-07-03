class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        point_set = set()
        for p in points:
            point_set.add(tuple(p))

        min_area = float('inf')
        n = len(points)

        for i in range(n):
            p1 = points[i]
            x1, y1 = p1[0], p1[1]

            for j in range(i + 1, n):
                p2 = points[j]
                x2, y2 = p2[0], p2[1]

                if x1 == x2 or y1 == y2:
                    continue

                p3_candidate = (x1, y2)
                p4_candidate = (x2, y1)

                if p3_candidate in point_set and p4_candidate in point_set:
                    current_area = abs(x1 - x2) * abs(y1 - y2)
                    min_area = min(min_area, current_area)

        if min_area == float('inf'):
            return 0
        else:
            return min_area