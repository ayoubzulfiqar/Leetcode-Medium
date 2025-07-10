import collections

def calculate_election_results(votes):
    vote_counts = collections.Counter(votes)
    
    if not vote_counts:
        return {}, [], 0

    max_votes = max(vote_counts.values())
    winners = [candidate for candidate, count in vote_counts.items() if count == max_votes]
    
    return vote_counts, winners, max_votes