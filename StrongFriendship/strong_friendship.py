import sys

N, M = map(int, sys.stdin.readline().split())

adj = [[False for _ in range(N)] for _ in range(N)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    adj[u][v] = True
    adj[v][u] = True

triangle_count = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if adj[i][j] and adj[j][k] and adj[k][i]:
                triangle_count += 1

print(triangle_count)