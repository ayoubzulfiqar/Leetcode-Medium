def find_top_scoring_students(students_data):
    if not students_data:
        return []

    max_score = max(student['score'] for student in students_data)

    top_students = []
    for student in students_data:
        if student['score'] == max_score:
            top_students.append(student)

    return top_students

if __name__ == '__main__':
    students_list1 = [
        {'name': 'Alice', 'score': 95},
        {'name': 'Bob', 'score': 88},
        {'name': 'Charlie', 'score': 95},
        {'name': 'David', 'score': 90}
    ]
    top_students1 = find_top_scoring_students(students_list1)
    print(top_students1)

    students_list2 = []
    top_students2 = find_top_scoring_students(students_list2)
    print(top_students2)

    students_list3 = [{'name': 'Eve', 'score': 100}]
    top_students3 = find_top_scoring_students(students_list3)
    print(top_students3)

    students_list4 = [
        {'name': 'Frank', 'score': 70},
        {'name': 'Grace', 'score': 70},
        {'name': 'Heidi', 'score': 70}
    ]
    top_students4 = find_top_scoring_students(students_list4)
    print(top_students4)