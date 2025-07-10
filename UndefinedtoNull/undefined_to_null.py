import math

def undefined_to_null(value):
    if value is None:
        return None
    if value == "":
        return None
    if value == []:
        return None
    if value == {}:
        return None
    if isinstance(value, float) and math.isnan(value):
        return None
    return value