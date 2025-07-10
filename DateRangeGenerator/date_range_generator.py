import datetime

def generate_date_range(start_date_str, end_date_str):
    start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()

    if start_date > end_date:
        return

    current_date = start_date
    one_day = datetime.timedelta(days=1)

    while current_date <= end_date:
        yield current_date
        current_date += one_day

if __name__ == '__main__':
    # Example 1: Generate dates for a standard range
    start_date_ex1 = "2023-01-01"
    end_date_ex1 = "2023-01-05"
    for date_obj in generate_date_range(start_date_ex1, end_date_ex1):
        print(date_obj.strftime('%Y-%m-%d'))

    # Example 2: Generate dates for a single day range
    start_date_ex2 = "2024-02-29"
    end_date_ex2 = "2024-02-29"
    for date_obj in generate_date_range(start_date_ex2, end_date_ex2):
        print(date_obj.strftime('%Y-%m-%d'))

    # Example 3: Generate dates for an invalid range (start date after end date)
    # This loop will not print anything as the generator will be empty.
    start_date_ex3 = "2023-12-25"
    end_date_ex3 = "2023-12-20"
    for date_obj in generate_date_range(start_date_ex3, end_date_ex3):
        print(date_obj.strftime('%Y-%m-%d'))