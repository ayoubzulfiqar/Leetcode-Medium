import collections

def find_winning_candidate(votes):
    if not votes:
        return None

    vote_counts = collections.Counter(votes)

    max_votes = 0
    for count in vote_counts.values():
        if count > max_votes:
            max_votes = count

    tied_candidates = []
    for candidate, count in vote_counts.items():
        if count == max_votes:
            tied_candidates.append(candidate)

    return min(tied_candidates)

if __name__ == "__main__":
    votes1 = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
    winner1 = find_winning_candidate(votes1)

    votes2 = ["Alice", "Bob", "Charlie", "Alice", "Bob", "Charlie"]
    winner2 = find_winning_candidate(votes2)

    votes3 = ["David"]
    winner3 = find_winning_candidate(votes3)

    votes4 = []
    winner4 = find_winning_candidate(votes4)

    votes5 = ["Zoe", "Anna", "Zoe", "Anna", "Ben"]
    winner5 = find_winning_candidate(votes5)

    votes6 = ["John", "John", "John", "John"]
    winner6 = find_winning_candidate(votes6)