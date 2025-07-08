import collections

class Solution:
    def networkBecomesIdle(self, edges: list[list[int]], patience: list[int]) -> int:
        n = len(patience)
        
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        dist = [-1] * n
        
        q = collections.deque()
        
        dist[0] = 0
        q.append(0)
        
        while q:
            u = q.popleft()
            
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        
        max_idle_time = 0
        
        for i in range(1, n):
            d = dist[i]
            p = patience[i]
            
            round_trip_time = 2 * d
            
            current_server_last_reply_arrival_time = 0
            
            if p >= round_trip_time:
                current_server_last_reply_arrival_time = round_trip_time
            else:
                last_send_time = ((round_trip_time - 1) // p) * p
                current_server_last_reply_arrival_time = last_send_time + round_trip_time
            
            max_idle_time = max(max_idle_time, current_server_last_reply_arrival_time)
            
        return max_idle_time + 1