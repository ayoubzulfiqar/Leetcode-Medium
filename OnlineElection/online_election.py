import collections
import bisect

class TopVotedCandidate:

    def __init__(self, persons: list[int], times: list[int]):
        self.leaders_at_time = []
        vote_counts = collections.defaultdict(int)
        current_leader = -1
        max_votes = 0

        for i in range(len(persons)):
            person = persons[i]
            time = times[i]

            vote_counts[person] += 1

            if vote_counts[person] >= max_votes:
                max_votes = vote_counts[person]
                current_leader = person
            
            self.leaders_at_time.append((time, current_leader))
        
        self.times_only = [entry[0] for entry in self.leaders_at_time]

    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times_only, t)
        
        return self.leaders_at_time[idx - 1][1]