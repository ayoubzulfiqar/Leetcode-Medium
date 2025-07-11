def find_visible_mountains(heights):
    if not heights:
        return 0

    visible_count = 0
    max_height_so_far = float('-inf')

    for height in heights:
        if height > max_height_so_far:
            visible_count += 1
            max_height_so_far = height
    
    return visible_count