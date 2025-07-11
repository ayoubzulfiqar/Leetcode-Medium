class Solution:
    def minCost(self, s: str) -> int:
        n = len(s)
        total_cost = 0
        
        for j in range(1, n):
            # If characters s[j] and s[j-1] are different,
            # we need to apply an operation to make them equal.
            # This is equivalent to flipping the "difference point" at index j.
            #
            # Option 1: Invert prefix s[0...