import collections

class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        graph = collections.defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        start_node = -1
        for node, neighbors in graph.items():
            if len(neighbors) == 1:
                start_node = node
                break
        
        n = len(adjacentPairs) + 1
        result = [0] * n
        
        result[0] = start_node
        
        prev_node = start_node
        current_node = graph[start_node][0]
        
        for i in range(1, n):
            result[i] = current_node
            
            next_node_candidates = graph[current_node]
            
            if len(next_node_candidates) == 1:
                # This is the last element, its only neighbor is the previous one.
                # No need to update current_node for the next iteration as there isn't one.
                pass
            else:
                # Find the neighbor that is not the prev_node
                if next_node_candidates[0] == prev_node:
                    next_node = next_node_candidates[1]
                else:
                    next_node = next_node_candidates[0]
                
                prev_node = current_node
                current_node = next_node
                
        return result