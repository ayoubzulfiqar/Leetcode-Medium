import collections

def analyze_subscription_conversion(user_activity_table):
    user_data = collections.defaultdict(lambda: {'free_trial_durations': [], 'paid_durations': [], 'activity_types': set()})

    for row in user_activity_table:
        user_id = row['user_id']
        activity_type = row['activity_type']
        activity_duration = row['activity_duration']

        user_data[user_id]['activity_types'].add(activity_type)
        if activity_type == 'free_trial':
            user_data[user_id]['free_trial_durations'].append(activity_duration)
        elif activity_type == 'paid':
            user_data[user_id]['paid_durations'].append(activity_duration)

    result = []
    for user_id, data in user_data.items():
        has_free_trial = 'free_trial' in data['activity_types']
        has_paid = 'paid' in data['activity_types']

        if has_free_trial and has_paid:
            trial_sum = sum(data['free_trial_durations'])
            trial_count = len(data['free_trial_durations'])
            trial_avg = trial_sum / trial_count

            paid_sum = sum(data['paid_durations'])
            paid_count = len(data['paid_durations'])
            paid_avg = paid_sum / paid_count

            result.append({
                'user_id': user_id,
                'trial_avg_duration': round(trial_avg, 2),
                'paid_avg_duration': round(paid_avg, 2)
            })

    result.sort(key=lambda x: x['user_id'])
    return result