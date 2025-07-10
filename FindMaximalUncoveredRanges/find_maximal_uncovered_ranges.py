def find_maximal_uncovered_ranges(total_start, total_end, covered_ranges):
    """
    Finds the maximal uncovered ranges within a given total range [total_start, total_end],
    considering a list of covered ranges. All ranges are inclusive.

    Args:
        total_start (int): The starting point of the total range.
        total_end (int): The ending point of the total range.
        covered_ranges (list of list of int): A list of [start, end] pairs representing
                                              the covered intervals.

    Returns:
        list of list of int: A list of [start, end] pairs representing the maximal
                              uncovered intervals within [total_start, total_end].
                              Returns an empty list if the entire range is covered.
    """

    # If there are no covered ranges, the entire total range is uncovered.
    if not covered_ranges:
        if total_start <= total_end:
            return [[total_start, total_end]]
        else:
            return [] # Invalid total range

    # 1. Sort the covered ranges by their start points.
    # This is crucial for correctly merging and finding gaps.
    covered_ranges.sort()

    # 2. Merge overlapping or adjacent covered ranges into a set of disjoint, maximal ranges.
    merged_ranges = []
    for current_range in covered_ranges:
        # If merged_ranges is empty, or the current range does not overlap/is not adjacent
        # to the last merged range, add it as a new merged range.
        # Adjacency check: current_range[0] > merged_ranges[-1][1] + 1
        if not merged_ranges or current_range[0] > merged_ranges[-1][1] + 1:
            merged_ranges.append(list(current_range)) # Use list() to avoid modifying original input if it's tuples
        else:
            # Overlap or adjacency: extend the end of the last merged range.
            merged_ranges[-1][1] = max(merged_ranges[-1][1], current_range[1])

    # 3. Find the uncovered gaps within the total range.
    uncovered_ranges = []
    current_uncovered_start = total_start

    for merged_range in merged_ranges:
        # Calculate the potential gap before the current merged range.
        # The gap starts from where the last uncovered segment ended (or total_start).
        # The gap ends just before the current merged range starts.
        gap_start = current_uncovered_start
        gap_end = merged_range[0] - 1

        # If a valid gap exists (start <= end) and it's within the total_end boundary
        if gap_start <= gap_end:
            # Ensure the gap's end does not exceed total_end
            if gap_start <= total_end: # Check if the gap actually starts within or before total_end
                uncovered_ranges.append([gap_start, min(gap_end, total_end)])

        # Update the current_uncovered_start to the point immediately after the current merged range ends.
        # We take max with current_uncovered_start to handle cases where a merged range starts
        # before total_start (e.g., total_start=5, merged_range=[0,7]). In such cases,
        # current_uncovered_start should not be moved back.
        current_uncovered_start = max(current_uncovered_start, merged_range[1] + 1)
        
        # Optimization: If the current_uncovered_start has already passed total_end,
        # no more uncovered ranges can exist within the total range.
        if current_uncovered_start > total_end:
            break

    # 4. After iterating through all merged ranges, check for any remaining uncovered range
    # at the end of the total range (i.e., after the last merged range).
    if current_uncovered_start <= total_end:
        uncovered_ranges.append([current_uncovered_start, total_end])

    return uncovered_ranges