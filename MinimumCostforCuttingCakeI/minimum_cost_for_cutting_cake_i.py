class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        total_cost = 0
        
        horizontal_pieces = 1 
        vertical_pieces = 1 

        i = 0
        j = 0

        while i < m - 1 or j < n - 1:
            if j == n - 1 or (i < m - 1 and horizontalCut[i] >= verticalCut[j]):
                total_cost += horizontalCut[i] * vertical_pieces
                horizontal_pieces += 1
                i += 1
            else:
                total_cost += verticalCut[j] * horizontal_pieces
                vertical_pieces += 1
                j += 1

        return total_cost