def get_most_experienced_project_employees(employees_data, project_employee_data):
    employee_experience_map = {emp[0]: emp[2] for emp in employees_data}

    project_employees = {}
    for project_id, employee_id in project_employee_data:
        if project_id not in project_employees:
            project_employees[project_id] = []
        project_employees[project_id].append(employee_id)

    results = []
    for project_id, assigned_employee_ids in project_employees.items():
        max_experience_for_project = -1

        for emp_id in assigned_employee_ids:
            if emp_id in employee_experience_map:
                max_experience_for_project = max(max_experience_for_project, employee_experience_map[emp_id])
        
        if max_experience_for_project != -1:
            for emp_id in assigned_employee_ids:
                if emp_id in employee_experience_map and employee_experience_map[emp_id] == max_experience_for_project:
                    results.append({'project_id': project_id, 'employee_id': emp_id})
    
    return results