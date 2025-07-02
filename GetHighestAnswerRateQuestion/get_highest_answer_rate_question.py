import collections

def get_highest_answer_rate_question(answers_data: list[tuple[int, str]]) -> int | None:
    if not answers_data:
        return None

    total_answers_per_question = collections.defaultdict(int)
    accepted_answers_per_question = collections.defaultdict(int)

    for question_id, answer_status in answers_data:
        total_answers_per_question[question_id] += 1
        if answer_status == 'accepted':
            accepted_answers_per_question[question_id] += 1

    max_rate = -1.0
    best_question_id = None

    sorted_qids = sorted(total_answers_per_question.keys())

    for qid in sorted_qids:
        total = total_answers_per_question[qid]
        accepted = accepted_answers_per_question[qid]

        current_rate = accepted / total
        
        if current_rate > max_rate:
            max_rate = current_rate
            best_question_id = qid

    return best_question_id