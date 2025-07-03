def find_smallest_common_element(rows):
    if not rows:
        return -1

    common_elements = set(rows[0])

    for i in range(1, len(rows)):
        current_row_set = set(rows[i])
        common_elements = common_elements.intersection(current_row_set)
        
        if not common_elements:
            return -1

    if common_elements:
        return min(common_elements)
    else:
        return -1