employees = [
    {"emp_id": 1, "emp_name": "Alice", "dept_id": 101},
    {"emp_id": 2, "emp_name": "Bob", "dept_id": 101},
    {"emp_id": 3, "emp_name": "Charlie", "dept_id": 102},
    {"emp_id": 4, "emp_name": "David", "dept_id": 101},
    {"emp_id": 5, "emp_name": "Eve", "dept_id": 103},
    {"emp_id": 6, "emp_name": "Frank", "dept_id": 102},
    {"emp_id": 7, "emp_name": "Grace", "dept_id": 103},
    {"emp_id": 8, "emp_name": "Heidi", "dept_id": 101},
    {"emp_id": 9, "emp_name": "Ivan", "dept_id": 104},
    {"emp_id": 10, "emp_name": "Julia", "dept_id": 101},
    {"emp_id": 11, "emp_name": "Kevin", "dept_id": 102},
    {"emp_id": 12, "emp_name": "Liam", "dept_id": 102},
    {"emp_id": 13, "emp_name": "Mia", "dept_id": 105},
]

departments = [
    {"dept_id": 101, "dept_name": "HR", "manager_id": 1},
    {"dept_id": 102, "dept_name": "Sales", "manager_id": 3},
    {"dept_id": 103, "dept_name": "Marketing", "manager_id": 5},
    {"dept_id": 104, "dept_name": "IT", "manager_id": 9},
    {"dept_id": 105, "dept_name": "Finance", "manager_id": 13},
]

dept_employee_counts = {}
for emp in employees:
    dept_id = emp["dept_id"]
    dept_employee_counts[dept_id] = dept_employee_counts.get(dept_id, 0) + 1

max_employees_count = 0
if dept_employee_counts:
    max_employees_count = max(dept_employee_counts.values())

largest_department_ids = []
for dept_id, count in dept_employee_counts.items():
    if count == max_employees_count:
        largest_department_ids.append(dept_id)

manager_ids_of_largest_depts = set()
for dept in departments:
    if dept["dept_id"] in largest_department_ids:
        manager_ids_of_largest_depts.add(dept["manager_id"])

emp_id_to_name = {emp["emp_id"]: emp["emp_name"] for emp in employees}

result_manager_names = []
for manager_id in manager_ids_of_largest_depts:
    if manager_id in emp_id_to_name:
        result_manager_names.append(emp_id_to_name[manager_id])

print(result_manager_names)