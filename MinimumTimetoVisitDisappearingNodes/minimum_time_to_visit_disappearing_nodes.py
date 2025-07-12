import heapq

class Solution:
    def minimumTime(self, n: int, edges: list[list[int]], disappear: list[int]) -> list[int]:
        adj = [[] for _ in range(n)]
        for u, v, length in edges:
            adj[u].append((v, length))
            adj[v].append((u, length))

        # Initialize distances. -1 indicates unreachable.
        dist = [-1] * n
        
        # Priority queue stores tuples of (time, node)
        # It will always pop the entry with the smallest time.
        pq = [(0, 0)] 
        
        # Starting node 0 takes 0 time to reach itself.
        dist[0] = 0

        while pq:
            current_time, u = heapq.heappop(pq)

            # If we have already found a shorter path to 'u',
            # or if 'u' has disappeared by the time we arrive via this path,
            # then this path is not optimal or valid, so skip.
            # The `dist[u] != -1` check is to ensure `dist[u]` has been set.
            if dist[u] != -1 and current_time > dist[u]:
                continue
            
            # If the current node 'u' has disappeared at or before 'current_time',
            # we cannot use it to travel further. The problem states "you won't be able to visit it"
            # at `disappear[i]`, implying arrival time must be strictly less than `disappear[i]`.
            if current_time >= disappear[u]:
                continue

            # Explore neighbors of 'u'
            for v, length in adj[u]:
                new_time = current_time + length

                # Check if this new path to 'v' is valid (i.e., 'v' hasn't disappeared yet)
                # AND if it's shorter than any previously found path to 'v'.
                if new_time < disappear[v]:
                    if dist[v] == -1 or new_time < dist[v]:
                        dist[v] = new_time
                        heapq.heappush(pq, (new_time, v))
        
        return dist