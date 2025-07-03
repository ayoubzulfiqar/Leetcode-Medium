class Solution:
    def findSmallestRegion(self, regions: list[list[str]], region1: str, region2: str) -> str:
        parent_map = {}
        for region_list in regions:
            parent = region_list[0]
            for i in range(1, len(region_list)):
                child = region_list[i]
                parent_map[child] = parent

        ancestors1 = set()
        current = region1
        while current in parent_map:
            ancestors1.add(current)
            current = parent_map[current]
        ancestors1.add(current) # Add the root ancestor of region1

        current = region2
        while current in parent_map:
            if current in ancestors1:
                return current
            current = parent_map[current]
        
        # After the loop, 'current' is the root of the path containing region2.
        # This root must be in ancestors1 (as it's the ultimate common ancestor).
        if current in ancestors1:
            return current
        
        # This line should ideally not be reached given the problem constraints
        # that all regions are part of a single hierarchy and a common region exists.
        return "" # Should not happen if problem guarantees are met

```