import collections
import math

def find_bursty_behavior(timestamps, bin_size, threshold_multiplier):
    if not timestamps:
        return []
    if len(timestamps) == 1:
        return []

    timestamps.sort()

    min_ts = timestamps[0]
    max_ts = timestamps[-1]

    # Normalize min_ts to the start of its bin
    start_time_normalized = (min_ts // bin_size) * bin_size
    # Determine the end time for binning to ensure all events are covered
    end_time_normalized = ((max_ts // bin_size) + 1) * bin_size

    bin_counts = collections.defaultdict(int)

    for ts in timestamps:
        bin_start = (ts // bin_size) * bin_size
        bin_counts[bin_start] += 1

    all_bin_starts = []
    current_bin_start = start_time_normalized
    while current_bin_start < end_time_normalized:
        all_bin_starts.append(current_bin_start)
        current_bin_start += bin_size

    counts = [bin_counts[b] for b in all_bin_starts]

    if not counts:
        return []

    mean_count = sum(counts) / len(counts)
    
    if len(counts) > 1:
        sum_sq_diff = sum((x - mean_count) ** 2 for x in counts)
        std_dev_count = math.sqrt(sum_sq_diff / (len(counts) - 1))
    else:
        std_dev_count = 0

    burst_threshold = mean_count + threshold_multiplier * std_dev_count

    burst_periods = []
    current_burst_start_index = -1

    for i, count in enumerate(counts):
        if count > burst_threshold:
            if current_burst_start_index == -1:
                current_burst_start_index = i
        else:
            if current_burst_start_index != -1:
                burst_start_time = all_bin_starts[current_burst_start_index]
                burst_end_time = all_bin_starts[i - 1] + bin_size
                burst_periods.append((burst_start_time, burst_end_time))
                current_burst_start_index = -1

    if current_burst_start_index != -1:
        burst_start_time = all_bin_starts[current_burst_start_index]
        burst_end_time = all_bin_starts[-1] + bin_size
        burst_periods.append((burst_start_time, burst_end_time))

    return burst_periods