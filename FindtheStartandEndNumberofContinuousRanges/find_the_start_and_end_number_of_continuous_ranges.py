def find_continuous_ranges(numbers):
    if not numbers:
        return []

    unique_sorted_numbers = sorted(list(set(numbers)))

    if not unique_sorted_numbers:
        return []

    ranges = []
    start_of_range = unique_sorted_numbers[0]

    for i in range(1, len(unique_sorted_numbers)):
        current_num = unique_sorted_numbers[i]
        previous_num = unique_sorted_numbers[i - 1]

        if current_num != previous_num + 1:
            ranges.append((start_of_range, previous_num))
            start_of_range = current_num

    ranges.append((start_of_range, unique_sorted_numbers[-1]))

    return ranges