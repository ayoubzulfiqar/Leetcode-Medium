import math

def find_top_percentile_fraud(data: list[float], percentile: int) -> list[float]:
    if not data:
        return []

    if percentile < 0:
        return []
    if percentile > 100:
        return sorted(data, reverse=True)

    sorted_data = sorted(data, reverse=True)

    n = len(sorted_data)
    
    num_elements = math.ceil(n * (percentile / 100.0))

    return sorted_data[:int(num_elements)]