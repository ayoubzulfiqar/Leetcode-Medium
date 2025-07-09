import collections

def calculate_driver_passenger_counts(trips_data):
    unique_drivers = set()
    passenger_counts = collections.Counter()

    for trip in trips_data:
        driver = trip["driver"]
        passengers = trip["passengers"]

        unique_drivers.add(driver)
        for passenger in passengers:
            passenger_counts[passenger] += 1

    result = {}
    for driver in unique_drivers:
        result[driver] = passenger_counts.get(driver, 0)
    
    return result

if __name__ == "__main__":
    trips_data = [
        {"driver": "Alice", "passengers": ["Bob", "Charlie"]},
        {"driver": "Bob", "passengers": ["Alice", "David"]},
        {"driver": "Charlie", "passengers": ["Bob"]},
        {"driver": "Alice", "passengers": ["Eve"]},
        {"driver": "David", "passengers": ["Alice", "Charlie"]},
        {"driver": "Frank", "passengers": ["Grace"]},
        {"driver": "Grace", "passengers": []},
        {"driver": "Bob", "passengers": ["Frank"]},
        {"driver": "Zoe", "passengers": ["Yara", "Xavier"]},
        {"driver": "Yara", "passengers": []},
        {"driver": "Xavier", "passengers": ["Zoe"]},
        {"driver": "Zoe", "passengers": ["Yara"]},
    ]

    driver_passenger_counts = calculate_driver_passenger_counts(trips_data)
    
    for driver, count in sorted(driver_passenger_counts.items()):
        print(f"{driver}: {count}")