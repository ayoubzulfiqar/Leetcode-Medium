import collections

def find_students_who_improved(scores_table):
    grouped_scores = collections.defaultdict(list)
    for row in scores_table:
        key = (row['student_id'], row['subject'])
        grouped_scores[key].append(row)

    improved_students = []
    for (student_id, subject), exams in grouped_scores.items():
        exams.sort(key=lambda x: x['exam_date'])

        if len(exams) >= 2:
            first_score = exams[0]['score']
            latest_score = exams[-1]['score']

            if latest_score > first_score:
                improved_students.append({
                    'student_id': student_id,
                    'subject': subject,
                    'first_score': first_score,
                    'latest_score': latest_score
                })

    improved_students.sort(key=lambda x: (x['student_id'], x['subject']))

    return improved_students