class Solution:
    def removeInterval(self, intervals: list[list[int]], toBeRemoved: list[int]) -> list[list[int]]:
        result = []
        remove_start, remove_end = toBeRemoved[0], toBeRemoved[1]

        for interval_start, interval_end in intervals:
            if interval_end <= remove_start or interval_start >= remove_end:
                # The current interval is completely outside the toBeRemoved interval.
                # It's either entirely to the left or entirely to the right.
                result.append([interval_start, interval_end])
            else:
                # There is an overlap.
                # Check for the part of the current interval that is to the left of toBeRemoved.
                if interval_start < remove_start:
                    result.append([interval_start, min(interval_end, remove_start)])

                # Check for the part of the current interval that is to the right of toBeRemoved.
                if interval_end > remove_end:
                    result.append([max(interval_start, remove_end), interval_end])
        
        return result