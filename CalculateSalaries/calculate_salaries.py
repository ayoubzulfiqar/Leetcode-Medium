def calculate_salaries(employees_data):
    """
    Calculates the total salary for each employee based on their hourly rate and hours worked.

    Args:
        employees_data (list of dict): A list where each dictionary represents an employee
                                       and contains 'name', 'hourly_rate', and 'hours_worked'.

    Returns:
        dict: A dictionary where keys are employee names and values are their calculated salaries.
              Returns None for a salary if input data for an employee is invalid.
    """
    salaries = {}
    for employee in employees_data:
        name = employee.get('name')
        hourly_rate = employee.get('hourly_rate')
        hours_worked = employee.get('hours_worked')

        if (isinstance(name, str) and
            isinstance(hourly_rate, (int, float)) and hourly_rate >= 0 and
            isinstance(hours_worked, (int, float)) and hours_worked >= 0):
            salary = hourly_rate * hours_worked
            salaries[name] = salary
        else:
            # Handle cases where data is incomplete or invalid for an employee
            salaries[name if name is not None else "Unknown Employee"] = None
    return salaries

if __name__ == "__main__":
    # Example employee data
    employee_records = [
        {'name': 'Alice Smith', 'hourly_rate': 25.0, 'hours_worked': 40},
        {'name': 'Bob Johnson', 'hourly_rate': 30.0, 'hours_worked': 35.5},
        {'name': 'Charlie Brown', 'hourly_rate': 20.0, 'hours_worked': 45},
        {'name': 'Diana Prince', 'hourly_rate': 28.5, 'hours_worked': 38.5},
        {'name': 'Eve Adams', 'hourly_rate': 15.0, 'hours_worked': 0},
        {'name': 'Frank White', 'hourly_rate': 50.0, 'hours_worked': 20},
        {'name': 'Grace Kelly', 'hourly_rate': None, 'hours_worked': 40}, # Invalid hourly rate
        {'name': 'Harry Potter', 'hourly_rate': 22.0, 'hours_worked': 'forty'}, # Invalid hours worked
        {'name': 'Invalid Employee', 'hourly_rate': -10.0, 'hours_worked': 30}, # Negative hourly rate
        {'name': 'Another Invalid', 'hourly_rate': 20.0, 'hours_worked': -5}, # Negative hours worked
        {'hourly_rate': 20.0, 'hours_worked': 30}, # Missing name
    ]

    # Calculate salaries
    calculated_salaries = calculate_salaries(employee_records)

    # Print results
    print("--- Salary Calculation Results ---")
    for name, salary in calculated_salaries.items():
        if salary is not None:
            print(f"{name}: ${salary:.2f}")
        else:
            print(f"{name}: Data invalid or incomplete, salary cannot be calculated.")

    print("\n--- Second Example Set ---")
    employee_records_2 = [
        {'name': 'Xavier', 'hourly_rate': 100, 'hours_worked': 10},
        {'name': 'Yara', 'hourly_rate': 75, 'hours_worked': 20.5},
    ]
    calculated_salaries_2 = calculate_salaries(employee_records_2)
    for name, salary in calculated_salaries_2.items():
        if salary is not None:
            print(f"{name}: ${salary:.2f}")
        else:
            print(f"{name}: Data invalid or incomplete, salary cannot be calculated.")