def find_candidates_for_data_scientist_position_ii(candidates):
    """
    Finds candidates suitable for a Data Scientist Position II based on specific criteria.

    Args:
        candidates (list of dict): A list of candidate dictionaries, each with:
            - 'id': int
            - 'name': str
            - 'experience_years': int
            - 'skills': list of str
            - 'education': str (e.g., 'Master of Science in Data Science')

    Returns:
        list of dict: A list of qualified candidate dictionaries.
    """
    qualified_candidates = []

    min_experience_years = 2
    required_core_skills = {'Python', 'SQL'}
    required_advanced_skills = {'Machine Learning', 'Deep Learning', 'Statistics', 'Predictive Modeling', 'NLP', 'Computer Vision'}
    required_education_degrees = {'Master', 'PhD', 'Doctorate'}
    required_education_fields = {'Data Science', 'Statistics', 'Computer Science', 'Mathematics', 'Physics', 'Engineering', 'Quantitative', 'Analytics'}

    for candidate in candidates:
        # Check experience
        if candidate.get('experience_years', 0) < min_experience_years:
            continue

        # Check core skills
        candidate_skills_set = set(skill.strip() for skill in candidate.get('skills', []))
        if not required_core_skills.issubset(candidate_skills_set):
            continue

        # Check advanced skills
        if not any(adv_skill in candidate_skills_set for adv_skill in required_advanced_skills):
            continue

        # Check education
        education_str = candidate.get('education', '').lower()
        has_required_degree = any(degree.lower() in education_str for degree in required_education_degrees)
        has_required_field = any(field.lower() in education_str for field in required_education_fields)

        if not (has_required_degree and has_required_field):
            continue

        qualified_candidates.append(candidate)

    return qualified_candidates

if __name__ == '__main__':
    # Example Usage:
    sample_candidates = [
        {
            'id': 1,
            'name': 'Alice Smith',
            'experience_years': 3,
            'skills': ['Python', 'SQL', 'Machine Learning', 'Data Visualization'],
            'education': 'Master of Science in Data Science'
        },
        {
            'id': 2,
            'name': 'Bob Johnson',
            'experience_years': 1,
            'skills': ['Python', 'SQL', 'Statistics'],
            'education': 'Bachelor of Science in Computer Science'
        },
        {
            'id': 3,
            'name': 'Charlie Brown',
            'experience_years': 5,
            'skills': ['Python', 'R', 'SQL', 'Deep Learning', 'Cloud Computing'],
            'education': 'PhD in Statistics'
        },
        {
            'id': 4,
            'name': 'Diana Prince',
            'experience_years': 2,
            'skills': ['Python', 'SQL', 'Tableau'],
            'education': 'Master of Business Administration' # Missing required advanced skill, not relevant field
        },
        {
            'id': 5,
            'name': 'Eve Adams',
            'experience_years': 4,
            'skills': ['Python', 'SQL', 'Predictive Modeling', 'NLP'],
            'education': 'Master of Engineering in Quantitative Finance'
        },
        {
            'id': 6,
            'name': 'Frank White',
            'experience_years': 2,
            'skills': ['Python', 'SQL', 'Machine Learning'],
            'education': 'Bachelor of Arts in Economics' # Not a Master's/PhD
        },
        {
            'id': 7,
            'name': 'Grace Lee',
            'experience_years': 3,
            'skills': ['Python', 'SQL', 'Statistics', 'Data Mining'],
            'education': 'Master of Science in Applied Mathematics'
        },
        {
            'id': 8,
            'name': 'Heidi King',
            'experience_years': 0, # Less than 2 years
            'skills': ['Python', 'SQL', 'Machine Learning'],
            'education': 'Master of Science in Data Science'
        },
        {
            'id': 9,
            'name': 'Ivan Petrov',
            'experience_years': 3,
            'skills': ['Python', 'SQL'], # Missing advanced skill
            'education': 'Master of Science in Computer Science'
        },
        {
            'id': 10,
            'name': 'Judy Hopps',
            'experience_years': 6,
            'skills': ['Python', 'SQL', 'Machine Learning', 'Big Data'],
            'education': 'Doctorate in Physics'
        }
    ]

    qualified_data_scientists = find_candidates_for_data_scientist_position_ii(sample_candidates)

    # Print the results (for demonstration purposes, not part of the strict output)
    # for candidate in qualified_data_scientists:
    #     print(f"Qualified: {candidate['name']} (ID: {candidate['id']})")
    # Expected qualified candidates: Alice Smith, Charlie Brown, Eve Adams, Grace Lee, Judy Hopps
    pass