import datetime

def analyze_game_play_iii(activity_data):
    """
    Analyzes game play data to find the activity date and the number of players
    who logged in for the first time on that date.

    Args:
        activity_data (list of dict): A list of dictionaries, where each dictionary
                                      represents a row from the 'Activity' table.
                                      Each dict should have 'player_id' (int) and
                                      'event_date' (str in 'YYYY-MM-DD' format).

    Returns:
        list of dict: A list of dictionaries, where each dictionary has
                      'install_date' (str in 'YYYY-MM-DD' format) and
                      'installs' (int), representing the number of players
                      who first logged in on that date.
    """
    player_first_login = {}

    # Step 1: Find the first login date for each player
    for record in activity_data:
        player_id = record['player_id']
        event_date_str = record['event_date']
        current_event_date = datetime.datetime.strptime(event_date_str, '%Y-%m-%d').date()

        if player_id not in player_first_login:
            player_first_login[player_id] = current_event_date
        else:
            if current_event_date < player_first_login[player_id]:
                player_first_login[player_id] = current_event_date

    # Step 2: Count players per first login date
    install_counts = {}
    for player_id, first_login_date in player_first_login.items():
        first_login_date_str = first_login_date.strftime('%Y-%m-%d')
        install_counts[first_login_date_str] = install_counts.get(first_login_date_str, 0) + 1

    # Step 3: Format the output
    result = []
    # Sort by date for consistent output, matching SQL ORDER BY behavior
    for install_date_str in sorted(install_counts.keys()):
        result.append({
            "install_date": install_date_str,
            "installs": install_counts[install_date_str]
        })

    return result