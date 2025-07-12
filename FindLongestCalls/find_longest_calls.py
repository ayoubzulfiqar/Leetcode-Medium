def find_longest_calls(calls):
    """
    Finds the call(s) with the maximum duration from a list of calls.

    Each call is expected to be a list or tuple of two elements:
    [start_time, end_time]. The duration is calculated as end_time - start_time.

    Args:
        calls: A list of calls, where each call is [start_time, end_time].

    Returns:
        A list of calls that have the maximum duration. If the input list
        is empty, an empty list is returned.
    """
    if not calls:
        return []

    max_duration = -1  # Initialize with a value lower than any possible valid duration
    longest_calls_list = []

    for call in calls:
        start_time = call[0]
        end_time = call[1]
        
        current_duration = end_time - start_time

        if current_duration > max_duration:
            max_duration = current_duration
            longest_calls_list = [call]  # Start a new list with this new longest call
        elif current_duration == max_duration:
            longest_calls_list.append(call)  # Add to the list of longest calls

    return longest_calls_list