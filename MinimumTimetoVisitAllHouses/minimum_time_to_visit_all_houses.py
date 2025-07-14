import heapq

class Solution:
    def minimumTime(self, heights: list[int]) -> int:
        n = len(heights)

        # If there's only one house, we are already there, so time is 0.
        if n == 1:
            return 0

        # dist[i] will store the minimum cost (time) to reach house i from house 0.
        # Initialize all distances to infinity, except for the starting house (house 0).
        dist = [float('inf')] * n
        dist[0] = 0

        # Priority queue to store (cost_to_reach_house, house_index).
        # It allows us to always retrieve the unvisited house with the smallest known cost.
        pq = [(0, 0)] # Start with house 0, which has a cost of 0 to reach itself.

        while pq:
            # Pop the house with the smallest cost from the priority queue.
            current_cost, u = heapq.heappop(pq)

            # If we have already found a shorter path to house u, skip this entry.
            # This can happen if a house is pushed to the PQ multiple times with different costs.
            if current_cost > dist[u]:
                continue

            # Explore neighbors of house u: house u-1 and house u+1.
            for v_offset in [-1, 1]:
                v = u + v_offset

                # Check if the neighbor house v is within the valid range [0, n-1].
                if 0 <= v < n:
                    # Calculate the cost to move from house u to house v.
                    # The cost is max(0, height_of_v - height_of_u), meaning
                    # there's a cost only when moving to a higher house (uphill).
                    # Moving downhill or to a house of the same height costs 0.
                    move_cost = max(0, heights[v] - heights[u])
                    
                    # If the path through u to v is shorter than the currently known path to v,
                    # update the distance to v and push it to the priority queue.
                    if dist[u] + move_cost < dist[v]:
                        dist[v] = dist[u] + move_cost
                        heapq.heappush(pq, (dist[v], v))

        # The problem asks for the minimum time to visit "all houses".
        # For a linear arrangement of houses starting at house 0, and allowing only adjacent moves,
        # visiting all houses implicitly means reaching house n-1 from house 0.
        # Any path from house 0 to house n-1 using only adjacent moves will necessarily
        # visit all intermediate houses. Therefore, the minimum time to visit all houses
        # is the minimum time to reach the last house (n-1).
        return dist[n - 1]