class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        result = []
        i, j = 0, 0
        n1, n2 = len(firstList), len(secondList)

        while i < n1 and j < n2:
            # Current intervals from both lists
            interval1 = firstList[i]
            interval2 = secondList[j]

            # Calculate the intersection start and end points
            low = max(interval1[0], interval2[0])
            high = min(interval1[1], interval2[1])

            # If there is an intersection, add it to the result
            if low <= high:
                result.append([low, high])

            # Advance the pointer of the interval that ends earlier
            # This is because the current interval from that list cannot intersect
            # with any future intervals from the other list.
            if interval1[1] < interval2[1]:
                i += 1
            else:
                j += 1
        
        return result