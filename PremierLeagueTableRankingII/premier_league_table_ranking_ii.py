import sys

def solve():
    teams_data = {}

    def get_team_stats(team_name):
        if team_name not in teams_data:
            teams_data[team_name] = {
                'name': team_name,
                'points': 0,
                'gd': 0, # Goal Difference
                'gf': 0, # Goals For
                'ga': 0, # Goals Against
                'mp': 0, # Matches Played
                'w': 0,  # Wins
                'd': 0,  # Draws
                'l': 0   # Losses
            }
        return teams_data[team_name]

    lines = sys.stdin.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        team1_name = parts[0]
        team2_name = parts[1]
        score_str = parts[2]

        score1, score2 = map(int, score_str.split('-'))

        team1_stats = get_team_stats(team1_name)
        team2_stats = get_team_stats(team2_name)

        team1_stats['mp'] += 1
        team1_stats['gf'] += score1
        team1_stats['ga'] += score2

        team2_stats['mp'] += 1
        team2_stats['gf'] += score2
        team2_stats['ga'] += score1

        if score1 > score2:
            team1_stats['points'] += 3
            team1_stats['w'] += 1
            team2_stats['l'] += 1
        elif score1 < score2:
            team2_stats['points'] += 3
            team2_stats['w'] += 1
            team1_stats['l'] += 1
        else:
            team1_stats['points'] += 1
            team1_stats['d'] += 1
            team2_stats['points'] += 1
            team2_stats['d'] += 1

    for team_name in teams_data:
        stats = teams_data[team_name]
        stats['gd'] = stats['gf'] - stats['ga']

    ranked_teams = list(teams_data.values())

    ranked_teams.sort(key=lambda x: (-x['points'], -x['gd'], -x['gf'], x['name']))

    for team in ranked_teams:
        print(f"{team['name']} {team['points']} {team['gd']} {team['gf']} {team['ga']} {team['mp']} {team['w']} {team['d']} {team['l']}")

solve()