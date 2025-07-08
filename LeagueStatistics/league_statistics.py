import re

def generate_league_statistics(matches):
    team_stats = {}

    def init_team(team_name):
        if team_name not in team_stats:
            team_stats[team_name] = {
                'P': 0, 'W': 0, 'D': 0, 'L': 0,
                'GF': 0, 'GA': 0, 'GD': 0, 'Pts': 0
            }

    for match_str in matches:
        match_pattern = re.compile(r"(.+?) vs (.+?): (\d+)-(\d+)")
        match = match_pattern.match(match_str)

        if not match:
            continue

        team1_name, team2_name, score1_str, score2_str = match.groups()
        score1 = int(score1_str)
        score2 = int(score2_str)

        init_team(team1_name)
        init_team(team2_name)

        team_stats[team1_name]['P'] += 1
        team_stats[team2_name]['P'] += 1

        team_stats[team1_name]['GF'] += score1
        team_stats[team1_name]['GA'] += score2
        team_stats[team2_name]['GF'] += score2
        team_stats[team2_name]['GA'] += score1

        if score1 > score2:
            team_stats[team1_name]['W'] += 1
            team_stats[team1_name]['Pts'] += 3
            team_stats[team2_name]['L'] += 1
        elif score2 > score1:
            team_stats[team2_name]['W'] += 1
            team_stats[team2_name]['Pts'] += 3
            team_stats[team1_name]['L'] += 1
        else:
            team_stats[team1_name]['D'] += 1
            team_stats[team1_name]['Pts'] += 1
            team_stats[team2_name]['D'] += 1
            team_stats[team2_name]['Pts'] += 1

    for team_name in team_stats:
        stats = team_stats[team_name]
        stats['GD'] = stats['GF'] - stats['GA']

    sorted_teams = sorted(
        team_stats.items(),
        key=lambda item: (
            -item[1]['Pts'],
            -item[1]['GD'],
            -item[1]['GF'],
            item[0]
        )
    )

    max_team_name_len = max(len(team_name) for team_name in team_stats) if team_stats else len("Team")
    team_col_width = max(max_team_name_len, 14)

    header_parts = ["Team".ljust(team_col_width), "P", "W", "D", "L", "GF", "GA", "GD", "Pts"]
    header_formatted = f"{header_parts[0]}{' '.join(h.rjust(3) for h in header_parts[1:])}"
    
    separator = "-" * len(header_formatted)

    print(header_formatted)
    print(separator)

    for team_name, stats in sorted_teams:
        line = (
            f"{team_name.ljust(team_col_width)}"
            f"{str(stats['P']).rjust(3)}"
            f"{str(stats['W']).rjust(3)}"
            f"{str(stats['D']).rjust(3)}"
            f"{str(stats['L']).rjust(3)}"
            f"{str(stats['GF']).rjust(3)}"
            f"{str(stats['GA']).rjust(3)}"
            f"{str(stats['GD']).rjust(3)}"
            f"{str(stats['Pts']).rjust(3)}"
        )
        print(line)