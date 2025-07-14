def find_overlapping_shifts(shifts):
    overlapping_shifts_set = set()
    n = len(shifts)

    for i in range(n):
        s1_start, s1_end = shifts[i]
        for j in range(i + 1, n):
            s2_start, s2_end = shifts[j]

            if max(s1_start, s2_start) < min(s1_end, s2_end):
                overlapping_shifts_set.add(shifts[i])
                overlapping_shifts_set.add(shifts[j])
    
    return sorted(list(overlapping_shifts_set))