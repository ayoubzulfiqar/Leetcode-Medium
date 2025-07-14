import heapq

class Solution:
    def countMentionsPerUser(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        mentions_count = [0] * numberOfUsers
        online_status = {i for i in range(numberOfUsers)}
        offline_queue = [] # Min-heap of (re_online_timestamp, user_id)

        sorted_events = []
        for event in events:
            event_type = event[0]
            timestamp = int(event[1])
            data = event[2]
            # OFFLINE events (type_order=0) processed before MESSAGE events (type_order=1) at same timestamp
            type_order = 0 if event_type == "OFFLINE" else 1
            sorted_events.append((timestamp, type_order, event_type, data))
        
        sorted_events.sort()

        for timestamp, _, event_type, data in sorted_events:
            # Process users coming back online from the offline_queue
            # This must happen before processing the current event
            while offline_queue and offline_queue[0][0] <= timestamp:
                re_online_time, user_id = heapq.heappop(offline_queue)
                online_status.add(user_id)

            # Process the current event
            if event_type == "OFFLINE":
                user_id = int(data)
                if user_id in online_status:
                    online_status.remove(user_id)
                heapq.heappush(offline_queue, (timestamp + 60, user_id))
            elif event_type == "MESSAGE":
                mentions_string = data
                if mentions_string == "ALL":
                    for i in range(numberOfUsers):
                        mentions_count[i] += 1
                elif mentions_string == "HERE":
                    for user_id in list(online_status): 
                        mentions_count[user_id] += 1
                else: # Specific user IDs like "id0 id1"
                    ids_str = mentions_string.split()
                    for id_str in ids_str:
                        user_id = int(id_str[2:]) # Extract number from "idX"
                        mentions_count[user_id] += 1
        
        return mentions_count