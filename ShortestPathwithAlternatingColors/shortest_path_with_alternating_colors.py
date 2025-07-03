import collections

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        adj_red = collections.defaultdict(list)
        for u, v in redEdges:
            adj_red[u].append(v)

        adj_blue = collections.defaultdict(list)
        for u, v in blueEdges:
            adj_blue[u].append(v)

        dist = [[float('inf')] * 2 for _ in range(n)]

        q = collections.deque()

        dist[0][0] = 0
        dist[0][1] = 0
        
        q.append((0, 0)) 
        q.append((0, 1))

        while q:
            u, prev_color = q.popleft()
            current_dist = dist[u][prev_color]

            next_color = 1 - prev_color

            if next_color == 0:
                for v in adj_red[u]:
                    if dist[v][0] > current_dist + 1:
                        dist[v][0] = current_dist + 1
                        q.append((v, 0))
            else: 
                for v in adj_blue[u]:
                    if dist[v][1] > current_dist + 1:
                        dist[v][1] = current_dist + 1
                        q.append((v, 1))

        answer = [-1] * n
        for i in range(n):
            min_dist_to_i = min(dist[i][0], dist[i][1])
            
            if min_dist_to_i != float('inf'):
                answer[i] = min_dist_to_i

        return answer