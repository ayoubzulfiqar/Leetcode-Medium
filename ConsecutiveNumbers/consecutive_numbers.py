def find_consecutive_numbers(logs_data):
    """
    Finds numbers that appear at least three times consecutively in the logs.

    Args:
        logs_data: A list of dictionaries, where each dictionary represents a row
                   with 'id' (int) and 'num' (str) keys.
                   Example: [{"id": 1, "num": "1"}, {"id": 2, "num": "1"}, ...]

    Returns:
        A list of integers representing the numbers that appear consecutively
        at least three times. The list is sorted for consistent output.
    """
    if not logs_data:
        return []

    consecutive_nums = set()
    
    prev_num = None
    count = 0

    for row in logs_data:
        current_num = row['num']

        if prev_num is None:
            # Initialize for the first element
            prev_num = current_num
            count = 1
        elif current_num == prev_num:
            # Same number, increment count
            count += 1
        else:
            # Different number, reset count and update previous
            prev_num = current_num
            count = 1
        
        # If count reaches 3 or more, add the number to the results
        if count >= 3:
            # Convert to int as per example output format
            consecutive_nums.add(int(current_num)) 
            
    # Return sorted list for consistent output, though order is not strictly required
    return sorted(list(consecutive_nums))