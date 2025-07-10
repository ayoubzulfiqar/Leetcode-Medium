import heapq

class Solution:
    def minimumCost(self, start: list[int], target: list[int], specialRoads: list[list[int]]) -> int:
        
        all_points_set = set()
        all_points_set.add(tuple(start))
        all_points_set.add(tuple(target))
        
        for s_road in specialRoads:
            all_points_set.add((s_road[0], s_road[1]))
            all_points_set.add((s_road[2], s_road[3]))
        
        all_points_list = list(all_points_set)
        point_to_idx = {point: i for i, point in enumerate(all_points_list)}
        
        num_nodes = len(all_points_list)
        start_idx = point_to_idx[tuple(start)]
        target_idx = point_to_idx[tuple(target)]
        
        dist = [float('inf')] * num_nodes
        dist[start_idx] = 0
        
        pq = [(0, start_idx)] # (cost, node_idx)
        
        while pq:
            d, u_idx = heapq.heappop(pq)
            
            if d > dist[u_idx]:
                continue
            
            u_point = all_points_list[u_idx]
            
            # Consider normal travel to all other points
            for v_idx in range(num_nodes):
                v_point = all_points_list[v_idx]
                normal_cost = abs(u_point[0] - v_point[0]) + abs(u_point[1] - v_point[1])
                
                if dist[u_idx] + normal_cost < dist[v_idx]:
                    dist[v_idx] = dist[u_idx] + normal_cost
                    heapq.heappush(pq, (dist[v_idx], v_idx))
            
            # Consider special roads starting from u_point
            for s_road in specialRoads:
                sx, sy, ex, ey, cost_s = s_road
                if u_point == (sx, sy):
                    v_point_s = (ex, ey)
                    v_idx_s = point_to_idx[v_point_s] 
                    
                    if dist[u_idx] + cost_s < dist[v_idx_s]:
                        dist[v_idx_s] = dist[u_idx] + cost_s
                        heapq.heappush(pq, (dist[v_idx_s], v_idx_s))
                        
        return dist[target_idx]