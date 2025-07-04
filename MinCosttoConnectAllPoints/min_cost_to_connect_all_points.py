import math

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        
        min_dist = [math.inf] * n
        in_mst = [False] * n
        
        total_cost = 0
        edges_connected = 0
        
        # Start with point 0. The cost to connect point 0 to itself is 0.
        min_dist[0] = 0
        
        # The loop runs n times, each time adding one point to the MST.
        while edges_connected < n:
            
            # Find the point u not yet in MST with the minimum min_dist value
            min_current_dist = math.inf
            u = -1
            
            for i in range(n):
                if not in_mst[i] and min_dist[i] < min_current_dist:
                    min_current_dist = min_dist[i]
                    u = i
            
            # If u is -1, it means no reachable unconnected node, which should not happen
            # in a graph where all points are reachable from each other.
            if u == -1:
                break
                
            # Add point u to MST
            in_mst[u] = True
            total_cost += min_current_dist
            edges_connected += 1
            
            # If all points are connected, we can stop.
            if edges_connected == n:
                break
            
            # Update min_dist for all neighbors (other points) of u
            # For each point v not yet in MST, calculate Manhattan distance to u
            # and update min_dist[v] if this new path is shorter.
            for v in range(n):
                if not in_mst[v]:
                    # Calculate Manhattan distance between points[u] and points[v]
                    dist_uv = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    
                    if dist_uv < min_dist[v]:
                        min_dist[v] = dist_uv
                        
        return total_cost