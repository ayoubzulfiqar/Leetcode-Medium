import datetime

def calculate_friday_purchases(purchases):
    total_friday_amount = 0.0
    for date_str, amount in purchases:
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        if date_obj.weekday() == 4:
            total_friday_amount += amount
    return total_friday_amount