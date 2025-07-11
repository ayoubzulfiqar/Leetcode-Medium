def deep_filter(obj, condition_func):
    if isinstance(obj, dict):
        filtered_dict = {}
        for k, v in obj.items():
            filtered_value = deep_filter(v, condition_func)
            if filtered_value is not None:
                filtered_dict[k] = filtered_value
        return filtered_dict if filtered_dict else None
    elif isinstance(obj, list):
        filtered_list = []
        for item in obj:
            filtered_item = deep_filter(item, condition_func)
            if filtered_item is not None:
                filtered_list.append(filtered_item)
        return filtered_list if filtered_list else None
    else:
        if condition_func(obj):
            return obj
        else:
            return None