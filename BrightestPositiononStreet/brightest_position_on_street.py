def brightestPosition(lights: list[list[int]]) -> int:
    events = []
    for pos, r in lights:
        # A light at pos with range r illuminates [pos - r, pos + r]
        # Start of interval: pos - r, brightness increases by 1
        events.append((pos - r, 1))
        # End of interval: pos + r, brightness decreases by 1 after this point
        # So, the effect stops at (pos + r + 1)
        events.append((pos + r + 1, -1))

    # Sort events:
    # 1. By coordinate (ascending)
    # 2. For same coordinate, process start events (type 1) before end events (type -1)
    #    Sorting by -type (1 comes before -1) achieves this.
    events.sort(key=lambda x: (x[0], -x[1]))

    current_brightness = 0
    max_brightness = 0
    brightest_position = 0 # This will be updated by the first event

    for coordinate, type_ in events:
        current_brightness += type_
        # If current_brightness strictly increases max_brightness,
        # this coordinate is the new brightest position.
        # Because events are sorted by coordinate, this ensures we pick the smallest x
        # among positions with maximum brightness.
        if current_brightness > max_brightness:
            max_brightness = current_brightness
            brightest_position = coordinate
    
    return brightest_position