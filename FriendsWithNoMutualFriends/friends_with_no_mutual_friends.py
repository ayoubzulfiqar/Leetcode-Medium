import collections

def friends_with_no_mutual_friends(friendships):
    graph = collections.defaultdict(set)
    for p1, p2 in friendships:
        graph[p1].add(p2)
        graph[p2].add(p1)

    result_pairs = set()

    for p1, p2 in friendships:
        mutual_friends = graph[p1].intersection(graph[p2])

        if not mutual_friends:
            sorted_pair = tuple(sorted((p1, p2)))
            result_pairs.add(sorted_pair)
            
    return sorted(list(result_pairs))