class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        max_overlap = 0

        # Iterate over all possible vertical shifts (dr)
        # dr ranges from -(n-1) to (n-1) inclusive.
        # A positive dr means img1 is effectively shifted downwards relative to img2's fixed position.
        # A negative dr means img1 is effectively shifted upwards.
        for dr in range(-(n - 1), n):
            # Iterate over all possible horizontal shifts (dc)
            # dc ranges from -(n-1) to (n-1) inclusive.
            # A positive dc means img1 is effectively shifted rightwards.
            # A negative dc means img1 is effectively shifted leftwards.
            for dc in range(-(n - 1), n):
                current_overlap = 0
                
                # Calculate the overlap for the current (dr, dc) translation.
                # We iterate through each cell (r, c) of the original img1.
                for r in range(n):
                    for c in range(n):
                        # If the current cell in img1 contains a 1,
                        # we check its corresponding position in img2 after translation.
                        if img1[r][c] == 1:
                            # Calculate the coordinates (r_shifted, c_shifted) where img1[r][c]
                            # would land in the img2's coordinate system after being shifted by (dr, dc).
                            r_shifted = r + dr
                            c_shifted = c + dc

                            # Check if this shifted position is within the valid bounds of img2.
                            # Bits translated outside the matrix borders are "erased" and don't contribute to overlap.
                            if 0 <= r_shifted < n and 0 <= c_shifted < n:
                                # If img2 also has a 1 at this corresponding position, it's an overlap.
                                if img2[r_shifted][c_shifted] == 1:
                                    current_overlap += 1
                
                # Update the maximum overlap found across all tested translations.
                max_overlap = max(max_overlap, current_overlap)
        
        return max_overlap