def json_deep_equal(obj1, obj2):
    if obj1 is obj2:
        return True

    if type(obj1) != type(obj2):
        return False

    if isinstance(obj1, (int, float, str, bool, type(None))):
        return obj1 == obj2

    if isinstance(obj1, (list, tuple)):
        if len(obj1) != len(obj2):
            return False
        for item1, item2 in zip(obj1, obj2):
            if not json_deep_equal(item1, item2):
                return False
        return True

    if isinstance(obj1, dict):
        if len(obj1) != len(obj2):
            return False
        if set(obj1.keys()) != set(obj2.keys()):
            return False
        for key in obj1:
            if not json_deep_equal(obj1[key], obj2[key]):
                return False
        return True

    return False