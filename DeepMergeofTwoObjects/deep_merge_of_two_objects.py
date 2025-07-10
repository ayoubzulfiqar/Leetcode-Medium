import copy

def deep_merge(obj1, obj2):
    if isinstance(obj1, dict) and isinstance(obj2, dict):
        merged = copy.deepcopy(obj1)
        for key, value in obj2.items():
            if key in merged and (isinstance(merged[key], (dict, list)) and isinstance(value, (dict, list))):
                merged[key] = deep_merge(merged[key], value)
            else:
                merged[key] = copy.deepcopy(value)
        return merged
    elif isinstance(obj1, list) and isinstance(obj2, list):
        merged_list = []
        len1 = len(obj1)
        len2 = len(obj2)
        max_len = max(len1, len2)

        for i in range(max_len):
            val1 = obj1[i] if i < len1 else None
            val2 = obj2[i] if i < len2 else None

            if val1 is not None and val2 is not None:
                merged_list.append(deep_merge(val1, val2))
            elif val1 is not None:
                merged_list.append(copy.deepcopy(val1))
            elif val2 is not None:
                merged_list.append(copy.deepcopy(val2))
        return merged_list
    else:
        return copy.deepcopy(obj2)