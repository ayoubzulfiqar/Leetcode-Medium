def last_person_to_fit(queue):
    WEIGHT_LIMIT = 1000

    sorted_queue = sorted(queue, key=lambda x: x['turn'])

    current_weight = 0
    last_person_name = None

    for person in sorted_queue:
        if current_weight + person['weight'] <= WEIGHT_LIMIT:
            current_weight += person['weight']
            last_person_name = person['person_name']
        else:
            break
    
    return [{"person_name": last_person_name}]

queue_data = [
    {"person_id": 5, "person_name": "Alice", "weight": 250, "turn": 1},
    {"person_id": 4, "person_name": "Bob", "weight": 175, "turn": 5},
    {"person_id": 3, "person_name": "Alex", "weight": 350, "turn": 2},
    {"person_id": 6, "person_name": "John Cena", "weight": 400, "turn": 3},
    {"person_id": 1, "person_name": "Winston", "weight": 500, "turn": 6},
    {"person_id": 2, "person_name": "Marie", "weight": 200, "turn": 4},
]

result = last_person_to_fit(queue_data)