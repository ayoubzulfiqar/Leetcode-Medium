import bisect

class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        events.sort(key=lambda x: (x[1], x[0]))

        n = len(events)

        dp = [0] * n
        dp[0] = events[0][2]
        for i in range(1, n):
            dp[i] = max(dp[i-1], events[i][2])

        max_total_value = dp[n-1]

        events_end_times = [event[1] for event in events]

        for i in range(n):
            current_start_time = events[i][0]
            current_value = events[i][2]

            idx = bisect.bisect_right(events_end_times, current_start_time - 1)

            if idx > 0:
                prev_event_max_val = dp[idx-1]
                max_total_value = max(max_total_value, current_value + prev_event_max_val)

        return max_total_value