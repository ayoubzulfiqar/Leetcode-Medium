def get_unique_participants(activities_data):
    unique_participants = set()
    for activity in activities_data:
        if 'participants' in activity and isinstance(activity['participants'], list):
            for participant in activity['participants']:
                unique_participants.add(participant)
    return sorted(list(unique_participants))