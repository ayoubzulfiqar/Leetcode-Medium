import math

class Solution:
    def waysToBuildHouseOfCards(self, n: int) -> int:
        # A house of cards structure can be defined by two parameters:
        # B: the number of triangles (A-frames) in the base level.
        # L: the number of levels in the house.
        #
        # For a valid house of cards, the number of triangles in each successive level
        # decreases by one, starting from B in the base level.
        # So, the levels have B, B-1, B-2, ..., B-(L-1) triangles.
        # The top level must have at least one triangle, so B-(L-1) >= 1, which implies B >= L.
        #
        # The number of cards required for a level with 't' triangles is (2*t + 1).
        # Total cards N for a house with L levels and B base triangles is the sum:
        # N = sum_{i=0}^{L-1} (2 * (B-i) + 1)
        # This sum can be simplified to:
        # N = (B - (B-L+1) + 1) * (B + (B-L+1) + 1) / 2 * 2  (sum of arithmetic series of terms (2*t+1))
        # Let k = B - L + 1 be the number of triangles in the top level.
        # The sequence of triangles per level is B, B-1, ..., k.
        # The number of levels L = B - k + 1.
        # The number of cards for this structure is:
        # N = (L/2) * ((2B+1) + (2k+1))
        # N = ( (B-k+1) / 2 ) * (2B + 2k + 2)
        # N = (B-k+1) * (B+k+1)
        #
        # Let x = B-k+1 (which is L, the number of levels)
        # Let y = B+k+1
        # So, N = x * y.
        #
        # We need to find pairs of integers (x, y) such that x * y = N.
        # From x and y, we can derive B and k:
        # Add the equations: x + y = (B-k+1) + (B+k+1) = 2B + 2  => B = (x+y)/2 - 1
        # Subtract the equations: y - x = (B+k+1) - (B-k+1) = 2k      => k = (y-x)/2
        #
        # For B and k to be valid integers representing a house of cards:
        # 1. x must be at least 1 (L >= 1).
        # 2. k must be at least 1 (top level has at least one triangle). This means (y-x)/2 >= 1 => y - x >= 2.
        # 3. B must be at least 1 (base has at least one