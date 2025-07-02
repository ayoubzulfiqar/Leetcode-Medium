class Solution:
    def minDistance(self, height: int, width: int, tree: list[int], squirrel: list[int], nuts: list[list[int]]) -> int:
        
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        total_base_dist = 0
        for nut in nuts:
            total_base_dist += 2 * manhattan_distance(nut, tree)
        
        min_delta_for_first_nut = float('inf') 
        
        for nut in nuts:
            squirrel_to_nut_dist = manhattan_distance(squirrel, nut)
            nut_to_tree_dist = manhattan_distance(nut, tree)
            
            current_delta = squirrel_to_nut_dist - nut_to_tree_dist
            min_delta_for_first_nut = min(min_delta_for_first_nut, current_delta)
            
        return total_base_dist + min_delta_for_first_nut