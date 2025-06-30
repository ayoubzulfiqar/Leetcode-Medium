class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        i = 0
        n = len(intervals)

        # Phase 1: Add all intervals that come completely before newInterval
        # (i.e., current_interval.end < newInterval.start)
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Phase 2: Merge newInterval with all overlapping intervals
        # (i.e., current_interval.start <= newInterval.end)
        # Note: Since intervals are sorted and we've passed all intervals before newInterval,
        # if intervals[i][0] <= newInterval[1], there must be an overlap.
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged newInterval to the result
        result.append(newInterval)

        # Phase 3: Add all intervals that come completely after the merged newInterval
        while i < n:
            result.append(intervals[i])
            i += 1

        return result