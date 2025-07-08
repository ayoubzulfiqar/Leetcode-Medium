class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        m = len(land)
        n = len(land[0])
        farmlands = []

        for r in range(m):
            for c in range(n):
                if land[r][c] == 1:
                    # Found the top-left corner of a new farmland group
                    r1, c1 = r, c

                    # Find the bottom-right corner (r2, c2)
                    # First, find the rightmost column (c2)
                    # Move right from (r1, c1) as long as we see '1's in the current row
                    temp_c = c1
                    while temp_c < n and land[r1][temp_c] == 1:
                        temp_c += 1
                    c2 = temp_c - 1 # Adjust back to the last '1' column

                    # Then, find the bottommost row (r2)
                    # Move down from (r1, c1) as long as we see '1's in the current column
                    temp_r = r1
                    while temp_r < m and land[temp_r][c1] == 1:
                        temp_r += 1
                    r2 = temp_r - 1 # Adjust back to the last '1' row
                    
                    # Add the group coordinates to the result list
                    farmlands.append([r1, c1, r2, c2])

                    # Mark all cells within this identified farmland group as visited (0)
                    # to prevent re-processing them as new groups
                    for i in range(r1, r2 + 1):
                        for j in range(c1, c2 + 1):
                            land[i][j] = 0
        
        return farmlands