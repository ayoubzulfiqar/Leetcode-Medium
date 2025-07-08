class Candidate:
    """
    Represents a candidate with their interview details.
    """
    def __init__(self, name: str, interview_score: int, years_of_experience: int, passed_technical_round: bool):
        self.name = name
        self.interview_score = interview_score
        self.years_of_experience = years_of_experience
        self.passed_technical_round = passed_technical_round

    def __repr__(self):
        return (f"Candidate(name='{self.name}', score={self.interview_score}, "
                f"experience={self.years_of_experience}, technical_passed={self.passed_technical_round})")

def get_accepted_candidates(candidates: list[Candidate], min_score: int, min_experience: int) -> list[str]:
    """
    Determines which candidates are accepted based on predefined criteria.

    Args:
        candidates: A list of Candidate objects.
        min_score: The minimum interview score required for acceptance.
        min_experience: The minimum years of experience required for acceptance.

    Returns:
        A list of names of accepted candidates.
    """
    accepted_names = []
    for candidate in candidates:
        # Criteria for acceptance:
        # 1. Interview score must be greater than or equal to min_score.
        # 2. Years of experience must be greater than or equal to min_experience.
        # 3. Must have passed the technical round.
        if (candidate.interview_score >= min_score and
            candidate.years_of_experience >= min_experience and
            candidate.passed_technical_round):
            accepted_names.append(candidate.name)
    return accepted_names

if __name__ == "__main__":
    # Sample candidate data
    all_candidates = [
        Candidate("Alice Smith", 85, 3, True),
        Candidate("Bob Johnson", 60, 5, True),
        Candidate("Charlie Brown", 75, 1, True),
        Candidate("David Lee", 90, 2, True),
        Candidate("Eve Davis", 70, 4, False), # Failed technical round
        Candidate("Frank White", 95, 10, True),
        Candidate("Grace Taylor", 65, 2, True), # Low score
        Candidate("Henry Miller", 80, 0, True)  # Low experience
    ]

    # Define acceptance criteria
    required_min_score = 70
    required_min_experience = 2

    # Get the list of accepted candidates
    accepted_candidates_list = get_accepted_candidates(
        all_candidates,
        required_min_score,
        required_min_experience
    )

    # Print the results
    print("Accepted Candidates:")
    if accepted_candidates_list:
        for name in accepted_candidates_list:
            print(f"- {name}")
    else:
        print("No candidates met the acceptance criteria.")