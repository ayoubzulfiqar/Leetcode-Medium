from collections import Counter

def find_active_users(user_activities):
    activity_counts = Counter(user_activities)
    active_users = []
    for user_id, count in activity_counts.items():
        if count > 1:
            active_users.append(user_id)
    return sorted(active_users)

if __name__ == '__main__':
    user_log1 = [1, 2, 1, 3, 2, 1, 4, 5, 5]
    print(find_active_users(user_log1))

    user_log2 = [10, 20, 30, 10, 20, 10]
    print(find_active_users(user_log2))

    user_log3 = [100, 200, 300]
    print(find_active_users(user_log3))

    user_log4 = []
    print(find_active_users(user_log4))

    user_log5 = [1, 1, 1, 1]
    print(find_active_users(user_log5))