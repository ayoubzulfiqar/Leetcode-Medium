class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        count_kept = 0
        last_end = float('-inf') 

        for interval in intervals:
            start, end = interval
            
            if start >= last_end:
                count_kept += 1
                last_end = end
            
        return len(intervals) - count_kept