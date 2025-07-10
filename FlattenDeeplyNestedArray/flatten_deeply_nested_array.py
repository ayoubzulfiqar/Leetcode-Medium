def flatten(arr: list, n: int) -> list:
    result = []

    def _flatten_recursive(current_arr, current_depth):
        for item in current_arr:
            if isinstance(item, list) and current_depth < n:
                _flatten_recursive(item, current_depth + 1)
            else:
                result.append(item)
    
    _flatten_recursive(arr, 0)
    return result