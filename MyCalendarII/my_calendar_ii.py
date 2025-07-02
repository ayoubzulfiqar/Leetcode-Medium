class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:
        for os, oe in self.overlaps:
            if max(startTime, os) < min(endTime, oe):
                return False

        new_overlaps_to_add = []
        for bs, be in self.bookings:
            intersection_start = max(startTime, bs)
            intersection_end = min(endTime, be)
            if intersection_start < intersection_end:
                new_overlaps_to_add.append([intersection_start, intersection_end])

        self.bookings.append([startTime, endTime])

        all_intervals_for_merge = self.overlaps + new_overlaps_to_add
        self.overlaps = self._merge_intervals(all_intervals_for_merge)

        return True

    def _merge_intervals(self, intervals):
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            if not merged or interval[0] >= merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)