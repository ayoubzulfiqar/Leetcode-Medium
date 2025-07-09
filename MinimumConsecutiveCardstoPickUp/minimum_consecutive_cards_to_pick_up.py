def minimumCardPickup(cards: list[int]) -> int:
    last_seen = {}
    min_length = float('inf')

    for i, card in enumerate(cards):
        if card in last_seen:
            # Calculate the length of the current consecutive subarray
            # that contains the matching pair.
            # The length is (current_index - last_seen_index + 1)
            current_length = i - last_seen[card] + 1
            min_length = min(min_length, current_length)
        
        # Update the last seen index for the current card value to its current position
        last_seen[card] = i
    
    # If min_length is still infinity, it means no matching pair was found
    if min_length == float('inf'):
        return -1
    else:
        return min_length