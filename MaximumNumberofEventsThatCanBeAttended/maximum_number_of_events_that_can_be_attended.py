import heapq

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        # Sort events by their start day. If start days are the same,
        # the order doesn't strictly matter for correctness, but Python's
        # default sort will use the second element (end day) as a tie-breaker.
        events.sort()

        n = len(events)
        attended_events_count = 0
        
        # Min-heap to store end days of currently available events.
        # We always want to attend the event that ends earliest to free up days.
        min_heap = [] 
        
        # Pointer for the sorted events array
        event_idx = 0
        
        # Iterate through days. The maximum day can be 10^5.
        # The loop continues as long as there are events to consider (either
        # yet to be added from the sorted list or currently in the heap).
        day = 1 
        while event_idx < n or min_heap:
            # If there are no events currently available in the heap,
            # and there are still events to process from the sorted list,
            # jump the 'day' to the start day of the next available event.
            # This optimizes by skipping days with no active events.
            if not min_heap and event_idx < n:
                day = events[event_idx][0] 
            
            # Add all events that start on or before 'day' to the min-heap.
            # Since events are sorted by startDay, this effectively adds all
            # events whose startDay is equal to the current 'day' (or were
            # available earlier and haven't been added yet due to a day jump).
            while event_idx < n and events[event_idx][0] <= day:
                heapq.heappush(min_heap, events[event_idx][1]) # Push endDay
                event_idx += 1
            
            # Remove events from the min-heap whose endDay is less than the current 'day'.
            # These events have already expired and cannot be attended today.
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            
            # If there are still available events in the heap, attend one.
            # We attend the one that ends earliest (min_heap[0]).
            if min_heap:
                heapq.heappop(min_heap) # Attend this event
                attended_events_count += 1
            
            # Move to the next day.
            day += 1
            
        return attended_events_count