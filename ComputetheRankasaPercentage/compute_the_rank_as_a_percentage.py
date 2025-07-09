def compute_rank_percentage(scores, target_score):
    num_scores = len(scores)
    if num_scores == 0:
        return 0.0
    rank = sum(1 for score in scores if score > target_score) + 1
    percentage = (rank / num_scores) * 100.0
    return percentage