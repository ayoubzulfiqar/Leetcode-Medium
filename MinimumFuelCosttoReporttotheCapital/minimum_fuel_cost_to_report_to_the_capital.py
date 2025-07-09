import collections
import math

class Solution:
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        adj = collections.defaultdict(list)
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)

        self.total_fuel = 0

        def dfs(node: int, parent: int) -> int:
            people_count = 1

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                
                people_from_child_subtree = dfs(neighbor, node)
                
                people_count += people_from_child_subtree
                
                cars_needed = (people_from_child_subtree + seats - 1) // seats
                self.total_fuel += cars_needed
            
            return people_count

        dfs(0, -1)
        
        return self.total_fuel