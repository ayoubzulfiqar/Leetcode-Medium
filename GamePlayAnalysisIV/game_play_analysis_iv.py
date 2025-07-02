import pandas as pd

def game_play_analysis_iv(activity: pd.DataFrame) -> pd.DataFrame:
    activity['event_date'] = pd.to_datetime(activity['event_date'])

    first_login_dates = activity.groupby('player_id')['event_date'].min().reset_index()
    first_login_dates.columns = ['player_id', 'first_login_date']

    merged_activity = pd.merge(activity, first_login_dates, on='player_id', how='left')

    consecutive_logins = merged_activity[
        merged_activity['event_date'] == (merged_activity['first_login_date'] + pd.Timedelta(days=1))
    ]

    players_with_consecutive_login = consecutive_logins['player_id'].nunique()
    total_players = activity['player_id'].nunique()

    if total_players == 0:
        fraction = 0.00
    else:
        fraction = players_with_consecutive_login / total_players

    result = pd.DataFrame({'fraction': [round(fraction, 2)]})

    return result