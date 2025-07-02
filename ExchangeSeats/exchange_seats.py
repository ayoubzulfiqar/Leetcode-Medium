def exchange_seats(seat_table: list[dict]) -> list[dict]:
    if not seat_table:
        return []

    students_map = {s['id']: s['student'] for s in seat_table}
    max_id = len(seat_table)
    
    result_list = [None] * max_id

    for i in range(1, max_id + 1, 2):
        current_id = i
        next_id = i + 1

        if next_id <= max_id:
            student_at_current = students_map[current_id]
            student_at_next = students_map[next_id]

            result_list[current_id - 1] = {'id': current_id, 'student': student_at_next}
            result_list[next_id - 1] = {'id': next_id, 'student': student_at_current}
        else:
            student_at_current = students_map[current_id]
            result_list[current_id - 1] = {'id': current_id, 'student': student_at_current}

    return result_list