class Solution:
    def describeThePainting(self, segments: list[list[int]]) -> list[list[int]]:
        events = []
        for start, end, color in segments:
            events.append((start, 0, color))
            events.append((end, 1, color))

        events.sort()

        painting = []
        current_active_colors_sum = 0
        active_colors_set = set()

        if not events:
            return []
        
        last_point = events[0][0]

        for current_point, event_type, color in events:
            if current_point > last_point:
                if current_active_colors_sum > 0:
                    painting.append([last_point, current_point, current_active_colors_sum])
            
            if event_type == 0:
                if color not in active_colors_set:
                    active_colors_set.add(color)
                    current_active_colors_sum += color
            else:
                if color in active_colors_set:
                    active_colors_set.remove(color)
                    current_active_colors_sum -= color
            
            last_point = current_point
        
        return painting