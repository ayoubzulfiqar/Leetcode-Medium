def find_top_performing_driver(drivers_data):
    """
    Finds the name of the top-performing driver based on their score.
    If multiple drivers share the highest score, the name of the first one encountered
    in the input list is returned.

    Args:
        drivers_data (list): A list of dictionaries, where each dictionary represents
                             a driver. Each driver dictionary is expected to have
                             at least 'name' (str) and 'score' (numeric) keys.
                             Example: [{'name': 'Driver A', 'score': 100},
                                       {'name': 'Driver B', 'score': 95}]

    Returns:
        str or None: The name of the top-performing driver. Returns None if the
                     input list is empty or contains no valid driver data.
    """
    if not drivers_data:
        return None

    top_driver_name = None
    max_score = float('-inf')

    for driver in drivers_data:
        if not isinstance(driver, dict):
            continue

        name = driver.get('name')
        score = driver.get('score')

        if not isinstance(name, str) or not isinstance(score, (int, float)):
            continue

        if score > max_score:
            max_score = score
            top_driver_name = name

    return top_driver_name