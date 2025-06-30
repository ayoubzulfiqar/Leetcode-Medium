def rank_scores(scores_table):
    unique_scores = sorted(list(set(item['score'] for item in scores_table)), reverse=True)
    
    score_to_rank_map = {}
    current_rank = 1
    for score in unique_scores:
        score_to_rank_map[score] = current_rank
        current_rank += 1
        
    ranked_scores = []
    for item in scores_table:
        score = item['score']
        rank = score_to_rank_map[score]
        ranked_scores.append({'score': score, 'rank': rank})
        
    final_result = sorted(ranked_scores, key=lambda x: x['score'], reverse=True)
    
    return final_result