class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        n = len(heights)
        ocean_view_buildings = []
        
        # Initialize max_height_to_right to -1, assuming heights are non-negative.
        # Any building with height >= 0 will be greater than -1.
        max_height_to_right = -1 

        # Iterate from right to left
        for i in range(n - 1, -1, -1):
            current_height = heights[i]
            
            # If the current building is taller than the tallest building found to its right so far,
            # it means this building has an ocean view.
            if current_height > max_height_to_right:
                ocean_view_buildings.append(i)
                # Update the maximum height encountered to the right
                max_height_to_right = current_height
        
        # The indices are collected in reverse order (from right to left),
        # so reverse the list to get them in increasing order as typically required.
        ocean_view_buildings.reverse()
        
        return ocean_view_buildings