import collections

class Solution:
    def rankTeams(self, votes: list[str]) -> str:
        if not votes:
            return ""
        
        num_teams = len(votes[0])
        
        team_counts = collections.defaultdict(lambda: [0] * num_teams)
        
        for vote in votes:
            for i, team in enumerate(vote):
                team_counts[team][i] += 1
        
        teams = list(votes[0])
        
        teams.sort(key=lambda team: tuple([-team_counts[team][i] for i in range(num_teams)] + [team]))
        
        return "".join(teams)