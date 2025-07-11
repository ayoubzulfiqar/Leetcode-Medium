import datetime
from collections import defaultdict

def find_peak_calling_hours(call_records):
    """
    Finds the peak calling hours for each city based on a list of call records.

    Args:
        call_records (list of dict): A list of dictionaries, where each dictionary
                                     represents a call record with 'city' and 'timestamp'.
                                     Example: [{'city': 'New York', 'timestamp': '2023-10-26 10:30:00'}]

    Returns:
        dict: A dictionary where keys are city names and values are lists of
              integers representing the peak calling hour(s) for that city.
              If multiple hours have the same maximum call count, all are included.
              Hours are sorted in ascending order.
              Returns an empty dictionary if no call records are provided.
    """
    city_hourly_counts = defaultdict(lambda: defaultdict(int))

    for record in call_records:
        city = record['city']
        timestamp_str = record['timestamp']
        
        # Parse the timestamp string to a datetime object
        # Assumes timestamp format "YYYY-MM-DD HH:MM:SS"
        dt_object = datetime.datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
        hour = dt_object.hour
        
        city_hourly_counts[city][hour] += 1

    peak_hours_by_city = {}

    for city, hourly_counts in city_hourly_counts.items():
        if not hourly_counts:
            continue # This case should not occur if city_hourly_counts is populated from call_records

        max_count = -1 
        current_peak_hours = []

        # Iterate through hourly counts to find the maximum count and collect all hours
        # that match this maximum count.
        for hour, count in hourly_counts.items():
            if count > max_count:
                max_count = count
                current_peak_hours = [hour] # Start a new list if a new maximum is found
            elif count == max_count:
                current_peak_hours.append(hour) # Add to list if it's a tie for the maximum
        
        # Sort the peak hours for consistent output order
        current_peak_hours.sort() 
        peak_hours_by_city[city] = current_peak_hours
        
    return peak_hours_by_city

if __name__ == "__main__":
    # Example usage with sample data
    sample_call_data = [
        {'city': 'New York', 'timestamp': '2023-10-26 10:30:00'},
        {'city': 'London', 'timestamp': '2023-10-26 10:45:00'},
        {'city': 'New York', 'timestamp': '2023-10-26 11:15:00'},
        {'city': 'London', 'timestamp': '2023-10-26 10:05:00'},
        {'city': 'New York', 'timestamp': '2023-10-26 10:55:00'},
        {'city': 'London', 'timestamp': '2023-10-26 11:30:00'},
        {'city': 'New York', 'timestamp': '2023-10-26 12:00:00'},
        {'city': 'London', 'timestamp': '2023-10-26 11:45:00'},
        {'city': 'New York', 'timestamp': '2023-10-26 10:01:00'}, # Another call for NY at 10
        {'city': 'London', 'timestamp': '2023-10-26 10:02:00'}, # Another call for London at 10
        {'city': 'London', 'timestamp': '2023-10-26 11:03:00'}, # Another call for London at 11
        {'city': 'Paris', 'timestamp': '2023-10-26 15:00:00'},
        {'city': 'Paris', 'timestamp': '2023-10-26 16:00:00'},
        {'city': 'Paris', 'timestamp': '2023-10-26 15:30:00'}, # Paris 15: 2 calls, Paris 16: 1 call
        {'city': 'Tokyo', 'timestamp': '2023-10-26 08:00:00'},
        {'city': 'Tokyo', 'timestamp': '2023-10-26 09:00:00'},
        {'city': 'Tokyo', 'timestamp': '2023-10-26 10:00:00'},
    ]

    peak_hours = find_peak_calling_hours(sample_call_data)
    print(peak_hours)

    # Test with empty data
    empty_data = []
    peak_hours_empty = find_peak_calling_hours(empty_data)
    print(peak_hours_empty)

    # Test with single city, single call
    single_call_data = [
        {'city': 'Rome', 'timestamp': '2023-10-26 09:00:00'}
    ]
    peak_hours_single = find_peak_calling_hours(single_call_data)
    print(peak_hours_single)

    # Test with a tie for peak hours
    tie_data = [
        {'city': 'Berlin', 'timestamp': '2023-10-26 14:00:00'},
        {'city': 'Berlin', 'timestamp': '2023-10-26 14:30:00'},
        {'city': 'Berlin', 'timestamp': '2023-10-26 15:00:00'},
        {'city': 'Berlin', 'timestamp': '2023-10-26 15:30:00'},
    ]
    peak_hours_tie = find_peak_calling_hours(tie_data)
    print(peak_hours_tie)