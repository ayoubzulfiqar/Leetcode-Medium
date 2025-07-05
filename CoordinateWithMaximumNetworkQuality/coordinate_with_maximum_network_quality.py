```python
import math

class Solution:
    def coordinateWithMaxNetworkQuality(self, towers: list[list[int]], radius: int) -> list[int]:
        max_quality = -1
        # Initialize best_coord to [0, 0] to satisfy the lexicographical
        # minimum non-negative coordinate requirement.
        # If all qualities are 0 (e.g., radius is too small for any tower to be reachable),
        # [0,0] will be returned as it's the lexicographically smallest.
        best_coord = [0, 0] 

        # The problem constraints state 0 <= xi, yi <= 50 and 1 <= radius <= 50.
        # This means the relevant search space for coordinates (cx, cy)
        # can extend from 0 (min tower coordinate) up to 50 (max tower coordinate) + 50 (max radius).
        # So, we need to check integer coordinates from 0 to 100 (inclusive) for both x and y.
        search_max_coord = 100 

        for cx in range(search_max_coord + 1):
            for cy in range(search_max_coord + 1):
                current_quality = 0
                for tx, ty, tq in towers:
                    # Calculate squared Euclidean distance to avoid float sqrt until necessary
                    dx = cx - tx
                    dy = cy - ty
                    d_squared = dx*dx + dy*dy
                    
                    # Check if the tower is reachable (distance <= radius)
                    # Comparing squared distance with squared radius avoids float precision issues
                    # with radius comparison and is slightly faster.
                    if d_squared <= radius*radius:
                        d = math.sqrt(d_squared)
                        
                        # Calculate signal quality using floor function
                        # math.floor ensures correct integer truncation for positive values
                        signal_quality = math.floor(tq / (1 + d))
                        current_quality += signal_quality
                
                # Update best_coord if a strictly higher quality is found.
                # Due to the nested loop order (cx iterates first, then cy),
                # if multiple coordinates have the same maximum quality, the first one
                # encountered (which will be the lexicographically smallest) will be stored.
                # Subsequent coordinates with the same quality will not overwrite it
                # because their quality is not *strictly greater*.
                if current_quality > max_quality:
                    max_quality = current_quality
                    best_coord = [cx, cy]
        
        return best_coord

```