class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        events = []
        for left, right in intervals:
            # For each interval, add a start event and an end event.
            # We use a tuple (coordinate, type) where type indicates if it's a start or end event.
            # Using 0 for start events and 1 for end events ensures that when events
            # at the same coordinate are sorted, start events are processed before end events.
            # This is crucial because intervals [a, b] and [b, c] are considered to intersect
            # if they share a common number (like 'b').
            events.append((left, 0))  # 0 indicates a start event
            events.append((right, 1)) # 1 indicates an end event
        
        # Sort the events.
        # Python's default tuple sorting first sorts by the first element (coordinate),
        # and then by the second element (event type) if the first elements are equal.
        # This means (coordinate, 0) will come before (coordinate, 1) for the same coordinate,
        # correctly handling the "intersect at endpoint" rule where an interval starting
        # at 'x' should be counted before an interval ending at 'x' decrements the count.
        events.sort()
        
        current_overlap = 0
        max_overlap = 0
        
        # Iterate through the sorted events to simulate a sweep line.
        for coordinate, event_type in events:
            if event_type == 0:  # It's a start event
                current_overlap += 1
            else:  # It's an end event
                current_overlap -= 1
            
            # Update the maximum overlap found so far.
            # The maximum value `current_overlap` reaches during the sweep
            # represents the maximum number of intervals that are simultaneously active.
            # This is equivalent to the minimum number of groups required, as each
            # simultaneously active interval needs to belong to a distinct group.
            max_overlap = max(max_overlap, current_overlap)
            
        return max_overlap