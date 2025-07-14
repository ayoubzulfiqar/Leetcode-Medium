import collections

def find_cities_in_each_state_ii(cities_data):
    state_to_cities = collections.defaultdict(list)
    for city, state in cities_data:
        state_to_cities[state].append(city)
    
    result = {}
    for state, cities in state_to_cities.items():
        if len(cities) >= 2:
            result[state] = cities
            
    return result