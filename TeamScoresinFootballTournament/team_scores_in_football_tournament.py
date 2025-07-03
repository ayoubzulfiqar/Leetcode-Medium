def calculate_team_scores(matches):
    team_points = {}

    for match in matches:
        team1, score1, team2, score2 = match

        if team1 not in team_points:
            team_points[team1] = 0
        if team2 not in team_points:
            team_points[team2] = 0

        if score1 > score2:
            team_points[team1] += 3
        elif score2 > score1:
            team_points[team2] += 3
        else:
            team_points[team1] += 1
            team_points[team2] += 1
            
    return team_points

if __name__ == "__main__":
    sample_matches = [
        ("TeamA", 2, "TeamB", 1),
        ("TeamC", 0, "TeamA", 0),
        ("TeamB", 3, "TeamC", 1),
        ("TeamD", 1, "TeamE", 0),
        ("TeamA", 1, "TeamD", 1)
    ]

    tournament_scores = calculate_team_scores(sample_matches)
    pass