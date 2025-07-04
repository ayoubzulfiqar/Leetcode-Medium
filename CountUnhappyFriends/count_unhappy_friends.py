def countUnhappyFriends(n, preferences, pairs):
    preference_rank = [[0] * n for _ in range(n)]
    for i in range(n):
        for rank, friend in enumerate(preferences[i]):
            preference_rank[i][friend] = rank

    paired_with = [0] * n
    for x, y in pairs:
        paired_with[x] = y
        paired_with[y] = x

    unhappy_count = 0
    for x in range(n):
        y = paired_with[x]
        
        for u in range(n):
            if u == x or u == y:
                continue

            v = paired_with[u]

            x_prefers_u_over_y = preference_rank[x][u] < preference_rank[x][y]
            u_prefers_x_over_v = preference_rank[u][x] < preference_rank[u][v]

            if x_prefers_u_over_y and u_prefers_x_over_v:
                unhappy_count += 1
                break

    return unhappy_count