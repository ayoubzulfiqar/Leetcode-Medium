import datetime

def find_users_with_two_purchases_within_seven_days(purchases):
    user_purchase_dates = {}
    for user_id, date_str in purchases:
        if user_id not in user_purchase_dates:
            user_purchase_dates[user_id] = []
        user_purchase_dates[user_id].append(datetime.datetime.strptime(date_str, '%Y-%m-%d').date())

    qualifying_users = set()
    seven_days = datetime.timedelta(days=7)

    for user_id, dates in user_purchase_dates.items():
        dates.sort() 

        if len(dates) < 2:
            continue

        left = 0
        for right in range(1, len(dates)):
            while dates[right] - dates[left] > seven_days:
                left += 1
            
            if right > left and dates[right] - dates[left] <= seven_days:
                qualifying_users.add(user_id)
                break 
                
    return sorted(list(qualifying_users))

if __name__ == "__main__":
    purchases_data = [
        (1, '2023-01-01'),
        (1, '2023-01-05'),
        (1, '2023-01-15'),

        (2, '2023-02-01'),
        (2, '2023-02-09'),

        (3, '2023-03-10'),
        (3, '2023-03-12'),
        (3, '2023-03-15'),

        (4, '2023-04-01'),

        (5, '2023-05-01'),
        (5, '2023-05-08'),

        (6, '2023-06-01'),
        (6, '2023-06-02'),
        (6, '2023-06-03'),

        (7, '2023-07-01'),
        (7, '2023-07-01'), 
        
        (8, '2023-08-10'),
        (8, '2023-08-17'),
        
        (9, '2023-09-01'),
        (9, '2023-09-08'),
        (9, '2023-09-15')
    ]

    result = find_users_with_two_purchases_within_seven_days(purchases_data)
    print(result)