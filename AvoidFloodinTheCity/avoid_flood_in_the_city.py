import collections
import bisect

class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        n = len(rains)
        ans = [0] * n  # Initialize with 0, will be -1 or lake_id
        
        # Stores lake_id -> last_rain_day_index
        # This tells us which lakes are currently full and when they became full.
        full_lakes = {} 
        
        # Stores indices of dry days (where rains[i] == 0)
        # This list will be kept sorted to efficiently find the next available dry day.
        dry_days = [] 
        
        for i in range(n):
            lake_id = rains[i]
            
            if lake_id > 0:  # It rains on a specific lake
                ans[i] = -1
                
                if lake_id in full_lakes:
                    # This lake is already full. We need to dry it.
                    # Find the earliest dry day *after* it last rained.
                    last_rain_day = full_lakes[lake_id]
                    
                    # Find the index of the first dry day in dry_days that is strictly greater than last_rain_day.
                    # bisect_left returns an insertion point. If we search for `last_rain_day + 1`,
                    # it will give us the index of the first element >= `last_rain_day + 1`.
                    idx_to_use = bisect.bisect_left(dry_days, last_rain_day + 1)
                    
                    if idx_to_use == len(dry_days):
                        # No dry day available after this lake last rained. Flood is unavoidable.
                        return []
                    
                    # Use this dry day to dry the current lake_id
                    dry_day_index = dry_days[idx_to_use]
                    ans[dry_day_index] = lake_id
                    
                    # Remove the used dry day from the list
                    dry_days.pop(idx_to_use)
                
                # Update the last rain day for this lake
                full_lakes[lake_id] = i
                
            else:  # rains[i] == 0, it's a dry day
                # We don't know which lake to dry yet. Add this day's index to dry_days.
                # We'll assign a lake to it later if a flood is imminent.
                # For now, assign a default value (e.g., 1) to ans[i].
                # This will be overwritten if this dry day is used to prevent a flood.
                # If it's not used, drying an arbitrary lake (like 1) is fine as it doesn't cause a flood.
                ans[i] = 1 # Default: dry lake 1 (arbitrary, as long as it's a valid lake ID)
                bisect.insort_left(dry_days, i) # Keep dry_days sorted
                
        return ans