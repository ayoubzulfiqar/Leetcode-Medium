import collections

def calculate_total_investment_2016(insurance_table: list[dict]) -> float:
    tiv_2015_values = [row["tiv_2015"] for row in insurance_table]
    location_coords = [(row["lat"], row["lon"]) for row in insurance_table]

    tiv_2015_counts = collections.Counter(tiv_2015_values)
    tiv_2015_duplicates = {val for val, count in tiv_2015_counts.items() if count > 1}

    location_counts = collections.Counter(location_coords)
    unique_locations = {loc for loc, count in location_counts.items() if count == 1}

    total_tiv_2016 = 0.0
    for row in insurance_table:
        current_tiv_2015 = row["tiv_2015"]
        current_location = (row["lat"], row["lon"])

        if current_tiv_2015 in tiv_2015_duplicates and current_location in unique_locations:
            total_tiv_2016 += row["tiv_2016"]

    result = round(total_tiv_2016, 2)

    return result