def max_potholes_fixed(potholes, budget):
    potholes.sort()
    fixed_count = 0
    current_budget = budget
    for pothole_size in potholes:
        if current_budget >= pothole_size:
            current_budget -= pothole_size
            fixed_count += 1
        else:
            break
    return fixed_count