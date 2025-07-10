def compactObject(obj: any) -> any:
    if isinstance(obj, dict):
        compacted_dict = {}
        for key, value in obj.items():
            if isinstance(value, (dict, list)):
                compacted_value = compactObject(value)
                compacted_dict[key] = compacted_value
            else:
                if bool(value):
                    compacted_dict[key] = value
        return compacted_dict
    elif isinstance(obj, list):
        compacted_list = []
        for element in obj:
            if isinstance(element, (dict, list)):
                compacted_element = compactObject(element)
                compacted_list.append(compacted_element)
            else:
                if bool(element):
                    compacted_list.append(element)
        return compacted_list