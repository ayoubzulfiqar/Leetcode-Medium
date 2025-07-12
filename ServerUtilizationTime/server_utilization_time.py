def calculate_server_utilization_time(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    merged_intervals = []
    merged_intervals.append(list(intervals[0]))

    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        last_merged_interval = merged_intervals[-1]

        if current_interval[0] <= last_merged_interval[1]:
            last_merged_interval[1] = max(last_merged_interval[1], current_interval[1])
        else:
            merged_intervals.append(list(current_interval))

    total_utilization_time = 0
    for start, end in merged_intervals:
        total_utilization_time += (end - start)

    return total_utilization_time

if __name__ == "__main__":
    print(calculate_server_utilization_time([[0, 2], [1, 3], [4, 5]]))
    print(calculate_server_utilization_time([[1, 5], [2, 4]]))
    print(calculate_server_utilization_time([[1, 2], [3, 4], [5, 6]]))
    print(calculate_server_utilization_time([]))
    print(calculate_server_utilization_time([[1, 10]]))
    print(calculate_server_utilization_time([[1, 3], [2, 4], [3, 5]]))
    print(calculate_server_utilization_time([[1, 5], [5, 7]]))
    print(calculate_server_utilization_time([[1, 5], [0, 2]]))
    print(calculate_server_utilization_time([[10, 20], [1, 5], [6, 8]]))