import datetime
import sys

input_lines = sys.stdin.readlines()

weekend_task_count = 0

for line in input_lines:
    date_str = line.strip()
    if not date_str:
        continue

    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        day_of_week = date_obj.weekday()
        if day_of_week == 5 or day_of_week == 6:
            weekend_task_count += 1
    except ValueError:
        pass

print(weekend_task_count)