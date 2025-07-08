from collections import defaultdict

def calculate_grand_slam_titles(title_records):
    player_titles = defaultdict(int)
    for player, _, _ in title_records:
        player_titles[player] += 1
    return dict(player_titles)