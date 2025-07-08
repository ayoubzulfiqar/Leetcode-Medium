import collections
import math

def find_cutoff_score_for_each_school(students_data):
    school_scores = collections.defaultdict(list)
    for student in students_data:
        school_scores[student['school']].append(student['score'])

    cutoff_scores = {}
    percentile_threshold = 75

    for school, scores in school_scores.items():
        if not scores:
            cutoff_scores[school] = None
            continue

        sorted_scores = sorted(scores)
        n = len(sorted_scores)

        index = math.ceil((percentile_threshold / 100.0) * n) - 1
        
        if index < 0:
            index = 0
        if index >= n:
            index = n - 1
        
        cutoff_scores[school] = sorted_scores[index]

    return cutoff_scores