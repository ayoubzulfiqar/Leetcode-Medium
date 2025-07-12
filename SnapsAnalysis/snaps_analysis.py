import math

def analyze_snaps(snaps_data):
    if not snaps_data:
        return {}

    total_snaps = len(snaps_data)
    
    first_snap_timestamp, first_snap_value = snaps_data[0]
    
    sum_values = first_snap_value
    min_value = first_snap_value
    max_value = first_snap_value
    min_value_timestamp = first_snap_timestamp
    max_value_timestamp = first_snap_timestamp
    min_timestamp = first_snap_timestamp
    max_timestamp = first_snap_timestamp

    for i in range(1, total_snaps):
        timestamp, value = snaps_data[i]
        
        sum_values += value
        
        if value > max_value:
            max_value = value
            max_value_timestamp = timestamp
        
        if value < min_value:
            min_value = value
            min_value_timestamp = timestamp
            
        if timestamp > max_timestamp:
            max_timestamp = timestamp
            
        if timestamp < min_timestamp:
            min_timestamp = timestamp

    average_value = sum_values / total_snaps
    time_duration = max_timestamp - min_timestamp

    results = {
        'total_snaps': total_snaps,
        'average_value': average_value,
        'max_value': max_value,
        'max_value_timestamp': max_value_timestamp,
        'min_value': min_value,
        'min_value_timestamp': min_value_timestamp,
        'time_duration': time_duration
    }
    
    return results

if __name__ == "__main__":
    sample_snaps = [
        (1678886400, 10.5),
        (1678886460, 12.1),
        (1678886520, 9.8),
        (1678886580, 15.3),
        (1678886640, 11.0),
        (1678886700, 8.7),
        (1678886760, 13.2)
    ]

    analysis_results = analyze_snaps(sample_snaps)
    pass