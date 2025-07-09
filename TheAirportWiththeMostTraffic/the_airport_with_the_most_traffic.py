from collections import defaultdict

def find_airport_with_most_traffic(flights):
    traffic_counts = defaultdict(int)

    for origin, destination in flights:
        traffic_counts[origin] += 1
        traffic_counts[destination] += 1

    if not traffic_counts:
        return ""

    airport_with_most_traffic = max(traffic_counts, key=traffic_counts.get)
    
    return airport_with_most_traffic