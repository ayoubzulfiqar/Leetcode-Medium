UNITS = {
    # Length (base: meter)
    'meter': ('length', 1.0, 0.0),
    'km': ('length', 1000.0, 0.0),
    'cm': ('length', 0.01, 0.0),
    'mm': ('length', 0.001, 0.0),
    'mile': ('length', 1609.344, 0.0),
    'yard': ('length', 0.9144, 0.0),
    'foot': ('length', 0.3048, 0.0),
    'inch': ('length', 0.0254, 0.0),

    # Mass (base: gram)
    'gram': ('mass', 1.0, 0.0),
    'kg': ('mass', 1000.0, 0.0),
    'mg': ('mass', 0.001, 0.0),
    'pound': ('mass', 453.59237, 0.0),
    'ounce': ('mass', 28.349523125, 0.0),

    # Volume (base: liter)
    'liter': ('volume', 1.0, 0.0),
    'ml': ('volume', 0.001, 0.0),
    'gallon': ('volume', 3.785411784, 0.0), # US liquid gallon
    'quart': ('volume', 0.946352946, 0.0),  # US liquid quart
    'pint': ('volume', 0.473176473, 0.0),   # US liquid pint
    'cup': ('volume', 0.2365882365, 0.0),   # US customary cup
    'floz': ('volume', 0.0295735295625, 0.0), # US fluid ounce

    # Temperature (base: Kelvin)
    # K = (value + offset) * multiplier
    # For Celsius: K = C + 273.15 => multiplier=1.0, offset=273.15
    # For Fahrenheit: K = (F + 459.67) * 5/9 => multiplier=5/9, offset=459.67
    'kelvin': ('temperature', 1.0, 0.0),
    'celsius': ('temperature', 1.0, 273.15),
    'fahrenheit': ('temperature', 5/9, 459.67),
}

def convert_units(value, from_unit, to_unit):
    """
    Converts a numerical value from one unit to another.

    Args:
        value (float or int): The numerical value to be converted.
        from_unit (str): The unit of the input value (e.g., 'meter', 'kg', 'celsius').
        to_unit (str): The desired unit for the output value.

    Returns:
        float: The converted value.

    Raises:
        ValueError: If the units are unknown or belong to different categories.
    """
    from_unit_info = UNITS.get(from_unit.lower())
    to_unit_info = UNITS.get(to_unit.lower())

    if not from_unit_info:
        raise ValueError(f"Unknown source unit: '{from_unit}'")
    if not to_unit_info:
        raise ValueError(f"Unknown target unit: '{to_unit}'")

    from_category, from_multiplier, from_offset = from_unit_info
    to_category, to_multiplier, to_offset = to_unit_info

    if from_category != to_category:
        raise ValueError(f"Cannot convert between '{from_category}' and '{to_category}' units.")

    if from_category == 'temperature':
        # Convert source value to base (Kelvin)
        value_in_base = (value + from_offset) * from_multiplier
        # Convert from base (Kelvin) to target unit
        converted_value = (value_in_base / to_multiplier) - to_offset
    else:
        # Convert source value to base unit
        value_in_base = value * from_multiplier
        # Convert from base unit to target unit
        converted_value = value_in_base / to_multiplier
    
    return converted_value

if __name__ == '__main__':
    # Example Usage:
    print(f"10 meters to feet: {convert_units(10, 'meter', 'foot'):.2f} ft")
    print(f"5 miles to km: {convert_units(5, 'mile', 'km'):.2f} km")
    print(f"100 inches to cm: {convert_units(100, 'inch', 'cm'):.2f} cm")

    print(f"2 kg to pounds: {convert_units(2, 'kg', 'pound'):.2f} lbs")
    print(f"16 ounces to grams: {convert_units(16, 'ounce', 'gram'):.2f} g")

    print(f"1 gallon to liters: {convert_units(1, 'gallon', 'liter'):.2f} L")
    print(f"500 ml to cups: {convert_units(500, 'ml', 'cup'):.2f} cups")
    print(f"10 floz to ml: {convert_units(10, 'floz', 'ml'):.2f} ml")

    print(f"0 Celsius to Fahrenheit: {convert_units(0, 'celsius', 'fahrenheit'):.2f} F")
    print(f"32 Fahrenheit to Celsius: {convert_units(32, 'fahrenheit', 'celsius'):.2f} C")
    print(f"273.15 Kelvin to Celsius: {convert_units(273.15, 'kelvin', 'celsius'):.2f} C")
    print(f"100 Celsius to Kelvin: {convert_units(100, 'celsius', 'kelvin'):.2f} K")

    # Error handling examples
    try:
        convert_units(10, 'meter', 'kg')
    except ValueError as e:
        print(f"Error: {e}")

    try:
        convert_units(10, 'unknown_unit', 'meter')
    except ValueError as e:
        print(f"Error: {e}")

    try:
        convert_units(10, 'meter', 'unknown_unit')
    except ValueError as e:
        print(f"Error: {e}")