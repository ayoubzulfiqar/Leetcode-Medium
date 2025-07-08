def find_interview_candidates(candidates, job_requirements):
    qualified_candidates_with_scores = []

    required_skills = set(job_requirements.get('required_skills', []))
    min_experience_years = job_requirements.get('min_experience_years', 0)
    required_education = job_requirements.get('required_education', 'High School')

    education_levels = {
        'High School': 0,
        'Associate': 1,
        'Bachelor': 2,
        'Master': 3,
        'PhD': 4
    }

    req_edu_level = education_levels.get(required_education, 0)

    for candidate in candidates:
        is_qualified = True
        score = 0

        candidate_skills = set(candidate.get('skills', []))
        candidate_experience = candidate.get('experience_years', 0)
        candidate_education = candidate.get('education', 'High School')
        candidate_edu_level = education_levels.get(candidate_education, 0)

        # Check Required Skills
        matched_skills = required_skills.intersection(candidate_skills)
        if len(matched_skills) < len(required_skills):
            is_qualified = False
        score += len(matched_skills)

        # Check Minimum Experience
        if candidate_experience < min_experience_years:
            is_qualified = False
        else:
            score += 1
            score += (candidate_experience - min_experience_years) * 0.5

        # Check Required Education
        if candidate_edu_level < req_edu_level:
            is_qualified = False
        else:
            score += 1
            score += (candidate_edu_level - req_edu_level) * 1.0

        if is_qualified:
            candidate_with_score = candidate.copy()
            candidate_with_score['score'] = score
            qualified_candidates_with_scores.append(candidate_with_score)

    qualified_candidates_with_scores.sort(key=lambda x: x['score'], reverse=True)

    final_candidates = []
    for c in qualified_candidates_with_scores:
        temp_c = c.copy()
        temp_c.pop('score', None)
        final_candidates.append(temp_c)

    return final_candidates