import itertools

def solve(data):
    person_followers = {}
    for row in data:
        if not row:
            continue
        person_id = row[0]
        followers = set(row[1:])
        person_followers[person_id] = followers

    people = sorted(list(person_followers.keys()))

    max_common = 0
    result_pairs = []

    if len(people) < 2:
        return []

    for p1, p2 in itertools.combinations(people, 2):
        common = len(person_followers[p1] & person_followers[p2])

        if common > max_common:
            max_common = common
            result_pairs = [[p1, p2]]
        elif common == max_common:
            result_pairs.append([p1, p2])
            
    return result_pairs