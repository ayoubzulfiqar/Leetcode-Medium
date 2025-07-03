def highest_grade_for_each_student(grades):
    """
    Calculates the highest grade for each student from a list of grade records.

    Args:
        grades: A list of tuples, where each tuple represents a grade record
                in the format (student_name: str, course_name: str, grade: int).

    Returns:
        A dictionary where keys are student names (str) and values are their
        highest grade (int).
    """
    student_highest_grades = {}
    for student_name, _, grade in grades:
        if student_name not in student_highest_grades or grade > student_highest_grades[student_name]:
            student_highest_grades[student_name] = grade
    return student_highest_grades

if __name__ == '__main__':
    # Example Usage:
    # Define a list of grade records
    grade_records = [
        ("Alice", "Math", 90),
        ("Bob", "Physics", 85),
        ("Alice", "Chemistry", 95),
        ("Bob", "Math", 70),
        ("Charlie", "Art", 100),
        ("Alice", "Physics", 88),
        ("Bob", "Chemistry", 92)
    ]

    # Get the highest grade for each student
    result = highest_grade_for_each_student(grade_records)
    print(result) # Expected: {'Alice': 95, 'Bob': 92, 'Charlie': 100}

    # Another example
    grade_records_2 = [
        ("David", "History", 75),
        ("Eve", "Biology", 80),
        ("David", "Geography", 82),
        ("Eve", "Chemistry", 78)
    ]
    result_2 = highest_grade_for_each_student(grade_records_2)
    print(result_2) # Expected: {'David': 82, 'Eve': 80}

    # Empty list case
    empty_records = []
    result_empty = highest_grade_for_each_student(empty_records)
    print(result_empty) # Expected: {}

    # Single student, single grade
    single_record = [("Frank", "Programming", 99)]
    result_single = highest_grade_for_each_student(single_record)
    print(result_single) # Expected: {'Frank': 99}