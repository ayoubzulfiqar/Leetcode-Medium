import heapq
import sys

class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: list[int], previousCost: list[int]) -> int:
        
        # Precompute minimum cost to transform any character to any other character.
        # min_char_cost[start_char_idx][end_char_idx] will store this minimum cost.
        min_char_cost = [[sys.maxsize] * 26 for _ in range(26)]

        # For each possible starting character (0 to 25, representing 'a' to 'z')
        for start_node in range(26):
            # Use Dijkstra's algorithm to find the shortest path (minimum cost)
            # from start_node to all other characters.
            
            # dist[i] stores the minimum cost found so far to transform start_node to character i.
            dist = [sys.maxsize] * 26
            dist[start_node] = 0
            
            # Priority queue stores tuples of (cost, current_char_index).
            # It prioritizes nodes with lower costs.
            pq = [(0, start_node)]
            
            while pq:
                current_cost, u = heapq.heappop(pq)
                
                # If we found a shorter path to u already, skip this one.
                if current_cost > dist[u]:
                    continue
                
                # Option 1: Shift to the next character in the alphabet.
                # The next character is (u + 1) % 26.
                # The cost for this shift is nextCost[u].
                v_next = (u + 1) % 26
                cost_to_v_next = nextCost[u]
                if dist[u] + cost_to_v_next < dist[v_next]:
                    dist[v_next] = dist[u] + cost_to_v_next
                    heapq.heappush(pq, (dist[v_next], v_next))
                
                # Option 2: Shift to the previous character in the alphabet.
                # The previous character is (u - 1 + 26) % 26 (add 26 to handle negative results from -1).
                # The cost for this shift is previousCost[u].
                v_prev = (u - 1 + 26) % 26 
                cost_to_v_prev = previousCost[u]
                if dist[u] + cost_to_v_prev < dist[v_prev]:
                    dist[v_prev] = dist[u] + cost_to_v_prev
                    heapq.heappush(pq, (dist[v_prev], v_prev))
            
            # After Dijkstra completes for start_node, dist contains all shortest paths
            # from start_node to every other character. Store these in min_char_cost.
            for end_node in range(26):
                min_char_cost[start_node][end_node] = dist[end_node]
        
        total_shift_distance = 0
        n = len(s)
        
        # Calculate the total shift distance by summing up the minimum costs
        # for transforming each character s[i] to t[i].
        for i in range(n):
            s_char_val = ord(s[i]) - ord('a')
            t_char_val = ord(t[i]) - ord('a')
            
            total_shift_distance += min_char_cost[s_char_val][t_char_val]
            
        return total_shift_distance