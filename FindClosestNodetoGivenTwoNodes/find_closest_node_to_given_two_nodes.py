import math

class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        n = len(edges)

        def get_distances(start_node: int, n_nodes: int, graph_edges: list[int]) -> list[int]:
            dists = [-1] * n_nodes
            current_node = start_node
            distance = 0
            while current_node != -1 and dists[current_node] == -1:
                dists[current_node] = distance
                current_node = graph_edges[current_node]
                distance += 1
            return dists

        dist1_arr = get_distances(node1, n, edges)
        dist2_arr = get_distances(node2, n, edges)

        min_max_dist = math.inf
        result_node = -1

        for i in range(n):
            if dist1_arr[i] != -1 and dist2_arr[i] != -1:
                current_max_dist = max(dist1_arr[i], dist2_arr[i])
                if current_max_dist < min_max_dist:
                    min_max_dist = current_max_dist
                    result_node = i
                # If current_max_dist == min_max_dist, we don't update result_node.
                # This ensures that result_node will hold the smallest index
                # among nodes that achieve the minimum maximum distance,
                # because we iterate 'i' in increasing order.

        return result_node