def get_second_highest_salary(employee_data):
    salaries = []
    for record in employee_data:
        salaries.append(record['salary'])
    
    distinct_salaries = sorted(list(set(salaries)), reverse=True)
    
    if len(distinct_salaries) >= 2:
        return distinct_salaries[1]
    else:
        return None