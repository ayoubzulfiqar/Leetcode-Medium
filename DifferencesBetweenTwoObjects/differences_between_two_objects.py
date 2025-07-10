def get_differences(obj1, obj2):
    diff = {}

    if obj1 == obj2:
        return diff

    if type(obj1) != type(obj2):
        diff['type_mismatch'] = {'old_type': str(type(obj1)), 'new_type': str(type(obj2))}
        diff['old_value'] = obj1
        diff['new_value'] = obj2
        return diff

    if isinstance(obj1, dict):
        added = {}
        removed = {}
        changed = {}

        for k, v1 in obj1.items():
            if k not in obj2:
                removed[k] = v1
            else:
                v2 = obj2[k]
                item_diff = get_differences(v1, v2)
                if item_diff:
                    changed[k] = item_diff

        for k, v2 in obj2.items():
            if k not in obj1:
                added[k] = v2

        if added:
            diff['added'] = added
        if removed:
            diff['removed'] = removed
        if changed:
            diff['changed'] = changed

    elif isinstance(obj1, (list, tuple)):
        changed_items = {}
        added_items = {}
        removed_items = {}

        len1 = len(obj1)
        len2 = len(obj2)

        min_len = min(len1, len2)

        for i in range(min_len):
            item_diff = get_differences(obj1[i], obj2[i])
            if item_diff:
                changed_items[f'[{i}]'] = item_diff

        if len2 > len1:
            for i in range(len1, len2):
                added_items[f'[{i}]'] = obj2[i]

        if len1 > len2:
            for i in range(len2, len1):
                removed_items[f'[{i}]'] = obj1[i]

        if changed_items:
            diff['changed_items'] = changed_items
        if added_items:
            diff['added_items'] = added_items
        if removed_items:
            diff['removed_items'] = removed_items
        
        if len1 != len2:
            diff['length_changed'] = {'old_length': len1, 'new_length': len2}

    else:
        diff['old_value'] = obj1
        diff['new_value'] = obj2

    return diff