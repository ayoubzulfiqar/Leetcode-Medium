def find_missing_ids(ids_list):
    if not ids_list:
        return []
    min_id = min(ids_list)
    max_id = max(ids_list)
    ids_set = set(ids_list)
    missing_ids = []
    for i in range(min_id, max_id + 1):
        if i not in ids_set:
            missing_ids.append(i)
    return missing_ids

if __name__ == "__main__":
    print(find_missing_ids([1, 2, 4, 5, 8]))
    print(find_missing_ids([10, 11, 12, 13]))
    print(find_missing_ids([]))
    print(find_missing_ids([7]))
    print(find_missing_ids([5, 10]))
    print(find_missing_ids([1, 2, 2, 4, 5]))