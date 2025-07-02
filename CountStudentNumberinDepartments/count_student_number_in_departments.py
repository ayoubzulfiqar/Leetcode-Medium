def count_students_per_department(students_list):
    department_counts = {}
    for student in students_list:
        department = student.get("department")
        if department:
            department_counts[department] = department_counts.get(department, 0) + 1
    return department_counts

students_data = [
    {"name": "Alice", "department": "Computer Science"},
    {"name": "Bob", "department": "Mathematics"},
    {"name": "Charlie", "department": "Computer Science"},
    {"name": "David", "department": "Physics"},
    {"name": "Eve", "department": "Mathematics"},
    {"name": "Frank", "department": "Computer Science"},
    {"name": "Grace", "department": "Chemistry"},
    {"name": "Heidi", "department": "Physics"},
    {"name": "Ivan", "department": "Chemistry"},
    {"name": "Judy", "department": "Biology"},
    {"name": "Karl", "department": "Mathematics"},
    {"name": "Liam", "department": "Computer Science"},
    {"name": "Mia", "department": "Biology"},
    {"name": "Nora", "department": "Chemistry"},
    {"name": "Oscar", "department": "Physics"},
    {"name": "Penny", "department": "Mathematics"},
    {"name": "Quinn", "department": "Computer Science"},
    {"name": "Rachel", "department": "Biology"},
    {"name": "Sam", "department": "Chemistry"},
    {"name": "Tina", "department": "Physics"},
    {"name": "Uma", "department": "Computer Science"},
    {"name": "Victor", "department": "Mathematics"},
    {"name": "Wendy", "department": "Biology"},
    {"name": "Xavier", "department": "Chemistry"},
    {"name": "Yara", "department": "Computer Science"},
    {"name": "Zoe", "department": "Physics"},
    {"name": "NoDeptStudent", "major": "Art"},
    {"name": "EmptyDeptStudent", "department": ""},
    {"name": "NoneDeptStudent", "department": None},
]

department_student_counts = count_students_per_department(students_data)

for department, count in department_student_counts.items():
    print(f"{department}: {count}")