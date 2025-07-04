import collections

def get_all_reporters(relations, given_manager_id):
    manager_to_direct_reports = collections.defaultdict(list)
    for employee, manager in relations:
        manager_to_direct_reports[manager].append(employee)

    all_reporters = []
    queue = collections.deque()

    if given_manager_id in manager_to_direct_reports:
        for direct_report in manager_to_direct_reports[given_manager_id]:
            queue.append(direct_report)
            all_reporters.append(direct_report)

    while queue:
        current_person = queue.popleft()
        if current_person in manager_to_direct_reports:
            for subordinate in manager_to_direct_reports[current_person]:
                all_reporters.append(subordinate)
                queue.append(subordinate)

    return sorted(list(set(all_reporters)))