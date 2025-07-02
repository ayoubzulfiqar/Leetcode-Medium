class Solution:
    def pourWater(self, heights: list[int], V: int, K: int) -> list[int]:
        n = len(heights)

        for _ in range(V):
            drop_idx = K

            # 1. Try to flow left
            # Search for the leftmost position where water can settle by flowing downhill or level.
            # If it encounters an uphill slope, it stops flowing in that direction.
            
            # current_search_idx tracks the current position being examined in the flow path
            # potential_drop_idx_left tracks the lowest point found so far in the current left path
            # min_height_in_path_left stores the height of the potential_drop_idx_left
            
            current_search_idx = K
            potential_drop_idx_left = K
            min_height_in_path_left = heights[K]

            for i in range(K - 1, -1, -1):
                if heights[i] < min_height_in_path_left:
                    # Found a new strictly lower point, this becomes the new potential drop spot
                    min_height_in_path_left = heights[i]
                    potential_drop_idx_left = i
                elif heights[i] > heights[current_search_idx]:
                    # Encountered an uphill slope (heights[i] is higher than heights[current_search_idx]),
                    # water cannot flow past this point to the left.
                    break
                current_search_idx = i # Continue searching left from the current pillar

            if potential_drop_idx_left != K:
                # Water found a lower spot to the left, it settles there
                drop_idx = potential_drop_idx_left
            else:
                # 2. If no lower spot was found to the left (or flow was blocked by an uphill slope),
                # try to flow right.
                # Similar logic for the right side.
                current_search_idx = K
                potential_drop_idx_right = K
                min_height_in_path_right = heights[K]

                for i in range(K + 1, n):
                    if heights[i] < min_height_in_path_right:
                        # Found a new strictly lower point
                        min_height_in_path_right = heights[i]
                        potential_drop_idx_right = i
                    elif heights[i] > heights[current_search_idx]:
                        # Encountered an uphill slope, cannot flow past this point to the right
                        break
                    current_search_idx = i # Continue searching right from the current pillar
                
                # Water settles at the rightmost lowest point found.
                # If no lower spot was found to the right, potential_drop_idx_right remains K,
                # meaning water settles at K.
                drop_idx = potential_drop_idx_right
            
            # Increment the height of the pillar where the unit of water settled
            heights[drop_idx] += 1
        
        return heights