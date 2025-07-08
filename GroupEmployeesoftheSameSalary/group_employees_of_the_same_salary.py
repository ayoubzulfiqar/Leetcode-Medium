import collections

def group_employees_by_salary(employees):
    grouped_employees = collections.defaultdict(list)
    for employee in employees:
        salary = employee['salary']
        grouped_employees[salary].append(employee)
    return dict(grouped_employees)

if __name__ == "__main__":
    employees_data = [
        {'name': 'Alice', 'salary': 50000},
        {'name': 'Bob', 'salary': 60000},
        {'name': 'Charlie', 'salary': 50000},
        {'name': 'David', 'salary': 70000},
        {'name': 'Eve', 'salary': 60000},
        {'name': 'Frank', 'salary': 50000},
        {'name': 'Grace', 'salary': 70000}
    ]

    grouped_result = group_employees_by_salary(employees_data)
    print(grouped_result)