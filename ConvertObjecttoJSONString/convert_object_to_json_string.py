import json

class SimpleObject:
    def __init__(self, name, value, is_active):
        self.name = name
        self.value = value
        self.is_active = is_active
        self.nested_data = {"id": 101, "type": "example"}
        self.items = ["item1", "item2"]

def convert_object_to_json_string(obj):
    """
    Converts a Python object to a JSON string.

    Args:
        obj: The object to convert. For simple custom objects,
             this function serializes its __dict__.
             For built-in types (dict, list, str, int, float, bool, None),
             it serializes them directly.
    Returns:
        A JSON string representation of the object.
    """
    if hasattr(obj, '__dict__'):
        return json.dumps(obj.__dict__)
    else:
        return json.dumps(obj)

if __name__ == "__main__":
    # Example 1: Custom object
    my_object = SimpleObject("TestObject", 123, True)
    json_string_from_object = convert_object_to_json_string(my_object)
    print(json_string_from_object)

    # Example 2: Dictionary (already JSON-serializable)
    my_dict = {"product_id": "P001", "name": "Laptop", "price": 1200.50, "in_stock": True}
    json_string_from_dict = convert_object_to_json_string(my_dict)
    print(json_string_from_dict)

    # Example 3: List
    my_list = [1, 2, "three", {"key": "value"}]
    json_string_from_list = convert_object_to_json_string(my_list)
    print(json_string_from_list)

    # Example 4: Basic type
    my_int = 42
    json_string_from_int = convert_object_to_json_string(my_int)
    print(json_string_from_int)