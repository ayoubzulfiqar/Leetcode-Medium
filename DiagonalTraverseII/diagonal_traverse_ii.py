class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        diagonals = {}
        
        # Group elements by their diagonal sum (row_idx + col_idx)
        # Elements are added to the list for each diagonal sum in increasing order
        # of their row index (and implicitly, decreasing order of column index
        # for a fixed sum).
        for r in range(len(nums)):
            for c in range(len(nums[r])):
                s = r + c
                if s not in diagonals:
                    diagonals[s] = []
                diagonals[s].append(nums[r][c])
        
        result = []
        
        # Iterate through diagonal sums in increasing order.
        # For each diagonal, the problem requires elements to be traversed
        # from bottom-left to top-right. This means for a fixed sum `s`,
        # elements with higher row indices should come before elements with
        # lower row indices.
        # Since we added elements in increasing row index order, we need to
        # reverse each diagonal's list.
        for s in sorted(diagonals.keys()):
            result.extend(reversed(diagonals[s]))
            
        return result