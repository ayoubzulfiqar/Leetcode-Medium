import heapq

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        # Sort the intervals by their start times.
        intervals.sort(key=lambda x: x[0])

        # Initialize a min-heap to store the end times of meetings.
        # The heap will always store the end times of meetings that are currently in progress.
        # The smallest element in the heap will be the meeting that ends earliest.
        min_heap = []

        # Add the first meeting's end time to the heap.
        # This meeting will occupy one room.
        heapq.heappush(min_heap, intervals[0][1])

        # Iterate through the rest of the intervals.
        for i in range(1, len(intervals)):
            current_start = intervals[i][0]
            current_end = intervals[i][1]

            # If the current meeting's start time is greater than or equal to
            # the earliest ending meeting in the heap (min_heap[0]),
            # it means that room becomes free.
            # So, we can reuse that room for the current meeting.
            if current_start >= min_heap[0]:
                heapq.heappop(min_heap) # Remove the meeting that just ended
            
            # In either case (reused a room or needed a new one),
            # add the current meeting's end time to the heap.
            # If a room was reused, the heap size remains the same.
            # If a new room was needed, the heap size increases by one.
            heapq.heappush(min_heap, current_end)
        
        # The maximum number of rooms needed at any point is the maximum size
        # the heap reached, which is equivalent to its final size after processing
        # all intervals.
        return len(min_heap)