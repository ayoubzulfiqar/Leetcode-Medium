import datetime

def solve():
    posts = [
        {'post_id': 1, 'post_date': '2019-06-01', 'user_id': 101},
        {'post_id': 2, 'post_date': '2019-06-02', 'user_id': 102},
        {'post_id': 3, 'post_date': '2019-07-01', 'user_id': 101},
        {'post_id': 4, 'post_date': '2019-07-02', 'user_id': 103},
        {'post_id': 5, 'post_date': '2019-07-03', 'user_id': 104},
    ]

    reports = [
        {'report_id': 1, 'reporter_id': 201, 'post_id': 1, 'report_date': '2019-07-01'},
        {'report_id': 2, 'reporter_id': 202, 'post_id': 2, 'report_date': '2019-07-01'},
        {'report_id': 3, 'reporter_id': 201, 'post_id': 3, 'report_date': '2019-07-02'},
        {'report_id': 4, 'reporter_id': 203, 'post_id': 4, 'report_date': '2019-07-03'},
        {'report_id': 5, 'reporter_id': 204, 'post_id': 5, 'report_date': '2019-07-04'},
        {'report_id': 6, 'reporter_id': 201, 'post_id': 5, 'report_date': '2019-07-05'},
        {'report_id': 7, 'reporter_id': 205, 'post_id': 1, 'report_date': '2019-06-30'},
        {'report_id': 8, 'reporter_id': 206, 'post_id': 2, 'report_date': '2019-07-06'},
    ]

    actions = [
        {'action_id': 1, 'reporter_id': 201, 'action': 'spam', 'action_date': '2019-06-15'},
        {'action_id': 2, 'reporter_id': 202, 'action': 'banned', 'action_date': '2019-07-01'},
        {'action_id': 3, 'reporter_id': 203, 'action': 'spam', 'action_date': '2019-07-02'},
        {'action_id': 4, 'reporter_id': 201, 'action': 'banned', 'action_date': '2019-07-03'},
        {'action_id': 5, 'reporter_id': 204, 'action': 'like', 'action_date': '2019-07-04'},
    ]

    start_date = datetime.date(2019, 7, 1)
    end_date = datetime.date(2019, 7, 5)

    banned_reporters = set()
    for action_row in actions:
        if action_row['action'] == 'banned':
            banned_reporters.add(action_row['reporter_id'])

    valid_reported_post_ids = set()
    for report_row in reports:
        report_date_obj = datetime.datetime.strptime(report_row['report_date'], '%Y-%m-%d').date()
        is_within_date_range = start_date <= report_date_obj <= end_date
        is_reporter_not_banned = report_row['reporter_id'] not in banned_reporters

        if is_within_date_range and is_reporter_not_banned:
            valid_reported_post_ids.add(report_row['post_id'])

    result = sorted(list(valid_reported_post_ids))
    
    return result