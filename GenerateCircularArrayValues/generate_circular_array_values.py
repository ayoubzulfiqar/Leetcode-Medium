def generate_circular_array(arr, length):
    if not arr:
        return []

    circular_arr = []
    for i in range(length):
        circular_arr.append(arr[i % len(arr)])
    return circular_arr