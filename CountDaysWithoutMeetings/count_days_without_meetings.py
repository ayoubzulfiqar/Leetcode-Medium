def countDaysWithoutMeetings(days: int, meetings: list[list[int]]) -> int:
    if not meetings:
        return days

    meetings.sort()

    merged_intervals = []
    for start, end in meetings:
        if not merged_intervals or start > merged_intervals[-1][1]:
            merged_intervals.append([start, end])
        else:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], end)

    total_meeting_days = 0
    for start, end in merged_intervals:
        total_meeting_days += (end - start + 1)
    
    return days - total_meeting_days