class Solution:
    def findContestMatch(self, n: int) -> str:
        teams = [str(i) for i in range(1, n + 1)]

        while len(teams) > 1:
            next_round_teams = []
            left = 0
            right = len(teams) - 1
            
            while left < right:
                match_str = "(" + teams[left] + "," + teams[right] + ")"
                next_round_teams.append(match_str)
                left += 1
                right -= 1
            
            teams = next_round_teams
            
        return teams[0]