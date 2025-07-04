import collections
from datetime import datetime, timedelta

def find_active_users(logs, k):
    user_dates = collections.defaultdict(set)
    for user_id, date_str in logs:
        user_dates[user_id].add(datetime.strptime(date_str, '%Y-%m-%d').date())

    active_users = set()

    for user_id, dates_set in user_dates.items():
        sorted_dates = sorted(list(dates_set))

        if len(sorted_dates) < k:
            continue

        consecutive_count = 1
        for i in range(1, len(sorted_dates)):
            if sorted_dates[i] == sorted_dates[i-1] + timedelta(days=1):
                consecutive_count += 1
            else:
                consecutive_count = 1

            if consecutive_count >= k:
                active_users.add(user_id)
                break

    return sorted(list(active_users))