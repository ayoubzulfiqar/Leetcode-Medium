def biggest_window_between_visits(visits: list[int]) -> int:
    if len(visits) < 2:
        return 0

    sorted_visits = sorted(visits)
    
    max_diff = 0
    for i in range(1, len(sorted_visits)):
        diff = sorted_visits[i] - sorted_visits[i-1]
        if diff > max_diff:
            max_diff = diff
            
    return max_diff