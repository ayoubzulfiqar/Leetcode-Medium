import heapq

class Solution:
    def smallestUnoccupiedChair(self, times: list[list[int]], targetFriend: int) -> int:
        n = len(times)

        events = []
        for i in range(n):
            arrival_time, leaving_time = times[i]
            # Event format: (time, event_type, friend_id)
            # event_type: 0 for leaving, 1 for arriving
            # This order ensures departures are processed before arrivals at the same time.
            events.append((arrival_time, 1, i))  # Friend i arrives
            events.append((leaving_time, 0, i))  # Friend i leaves

        # Sort events:
        # Primary sort key: time
        # Secondary sort key: event_type (0 (leaving) comes before 1 (arriving) for ties in time)
        events.sort()

        # Min-heap to store available chair numbers.
        # Chairs are added to this heap when they become free.
        # When a chair is needed, the smallest number is popped from here.
        available_chairs = [] 
        
        # The next available chair number to assign if `available_chairs` is empty.
        # This effectively tracks the highest chair number ever used + 1.
        next_chair_id = 0

        # Dictionary to store which chair each friend is currently occupying.
        # Maps friend_id to chair_number.
        friend_chair_map = {} 

        for time, event_type, friend_id in events:
            if event_type == 0:  # Friend is leaving
                # Retrieve the chair the friend was sitting on.
                chair_to_free = friend_chair_map[friend_id]
                # Make the chair available by pushing it to the min-heap.
                heapq.heappush(available_chairs, chair_to_free)
            else:  # event_type == 1, Friend is arriving
                chair = -1
                if available_chairs:
                    # If there are chairs already freed, take the smallest numbered one.
                    chair = heapq.heappop(available_chairs)
                else:
                    # If no chairs are currently available, assign a new chair
                    # with the next consecutive number.
                    chair = next_chair_id
                    next_chair_id += 1
                
                # Record which chair this friend sits on.
                friend_chair_map[friend_id] = chair

                # If this is the target friend, we have found their chair.
                if friend_id == targetFriend:
                    return chair

        # This line should ideally not be reached given the problem constraints
        # that targetFriend will always arrive and be assigned a chair.
        return -1