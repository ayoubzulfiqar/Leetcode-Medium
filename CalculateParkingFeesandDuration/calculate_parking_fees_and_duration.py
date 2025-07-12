import datetime
import math

def calculate_parking_fee_and_duration(entry_time_str, exit_time_str):
    time_format = "%Y-%m-%d %H:%M:%S"

    try:
        entry_time = datetime.datetime.strptime(entry_time_str, time_format)
        exit_time = datetime.datetime.strptime(exit_time_str, time_format)
    except ValueError:
        return 0.0, "Invalid time format"

    if exit_time < entry_time:
        return 0.0, "Exit time before entry time"

    duration = exit_time - entry_time
    total_seconds = duration.total_seconds()

    if total_seconds == 0:
        return 0.0, "0 hours 0 minutes"

    fee = 0.0
    # Fee structure:
    # - First hour (or part thereof): $5.00
    # - Each subsequent hour (or part thereof): $3.00

    if total_seconds <= 3600: # Up to and including 1 hour
        fee = 5.00
    else:
        fee = 5.00 # Base for the first hour
        remaining_seconds = total_seconds - 3600
        additional_hours_charged = math.ceil(remaining_seconds / 3600.0)
        fee += additional_hours_charged * 3.00

    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    duration_str = f"{hours} hours {minutes} minutes"

    return fee, duration_str

if __name__ == "__main__":
    entry1 = "2023-10-26 10:00:00"
    exit1 = "2023-10-26 10:30:00"
    fee1, duration1 = calculate_parking_fee_and_duration(entry1, exit1)
    print(f"Entry: {entry1}, Exit: {exit1} -> Fee: ${fee1:.2f}, Duration: {duration1}")

    entry2 = "2023-10-26 10:00:00"
    exit2 = "2023-10-26 11:00:00"
    fee2, duration2 = calculate_parking_fee_and_duration(entry2, exit2)
    print(f"Entry: {entry2}, Exit: {exit2} -> Fee: ${fee2:.2f}, Duration: {duration2}")

    entry3 = "2023-10-26 10:00:00"
    exit3 = "2023-10-26 11:00:01"
    fee3, duration3 = calculate_parking_fee_and_duration(entry3, exit3)
    print(f"Entry: {entry3}, Exit: {exit3} -> Fee: ${fee3:.2f}, Duration: {duration3}")

    entry4 = "2023-10-26 10:00:00"
    exit4 = "2023-10-26 12:00:00"
    fee4, duration4 = calculate_parking_fee_and_duration(entry4, exit4)
    print(f"Entry: {entry4}, Exit: {exit4} -> Fee: ${fee4:.2f}, Duration: {duration4}")

    entry5 = "2023-10-26 10:00:00"
    exit5 = "2023-10-26 12:00:01"
    fee5, duration5 = calculate_parking_fee_and_duration(entry5, exit5)
    print(f"Entry: {entry5}, Exit: {exit5} -> Fee: ${fee5:.2f}, Duration: {duration5}")

    entry6 = "2023-10-26 10:00:00"
    exit6 = "2023-10-26 10:00:00"
    fee6, duration6 = calculate_parking_fee_and_duration(entry6, exit6)
    print(f"Entry: {entry6}, Exit: {exit6} -> Fee: ${fee6:.2f}, Duration: {duration6}")

    entry7 = "2023-10-26 10:00:00"
    exit7 = "2023-10-26 09:00:00"
    fee7, duration7 = calculate_parking_fee_and_duration(entry7, exit7)
    print(f"Entry: {entry7}, Exit: {exit7} -> Fee: ${fee7:.2f}, Duration: {duration7}")

    entry8 = "invalid-time-format"
    exit8 = "2023-10-26 10:00:00"
    fee8, duration8 = calculate_parking_fee_and_duration(entry8, exit8)
    print(f"Entry: {entry8}, Exit: {exit8} -> Fee: ${fee8:.2f}, Duration: {duration8}")