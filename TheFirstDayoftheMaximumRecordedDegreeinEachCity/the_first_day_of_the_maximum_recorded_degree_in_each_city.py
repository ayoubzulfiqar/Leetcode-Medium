import collections

def get_first_day_of_max_degree(records):
    city_data = collections.defaultdict(list)
    for record in records:
        city_data[record['city']].append(record)

    result = []
    for city, city_records in city_data.items():
        max_degree = float('-inf')
        min_date_for_max_degree = "9999-12-31"

        for record in city_records:
            current_degree = record['degree']
            current_date = record['date']

            if current_degree > max_degree:
                max_degree = current_degree
                min_date_for_max_degree = current_date
            elif current_degree == max_degree:
                if current_date < min_date_for_max_degree:
                    min_date_for_max_degree = current_date
        
        result.append({
            "city": city,
            "first_max_degree_date": min_date_for_max_degree,
            "max_degree": max_degree
        })
    
    return result