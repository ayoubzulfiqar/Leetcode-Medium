class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])

        # Build 2D prefix sum array
        # P[r][c] stores sum of rectangle from (0,0) to (r-1, c-1)
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                P[r+1][c+1] = mat[r][c] + P[r][c+1] + P[r+1][c] - P[r][c]

        # Helper function to get sum of a square
        # (r1, c1) is top-left, (r2, c2) is bottom-right (inclusive)
        def get_square_sum(r1, c1, r2, c2):
            return P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]

        # Check if a square of side length 'k' exists with sum <= threshold
        def check(k):
            if k == 0:
                return True # A square of side 0 conceptually has sum 0, which is always <= threshold

            # Iterate through all possible top-left corners (r, c) for a k x k square
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    r1, c1 = r, c
                    r2, c2 = r + k - 1, c + k - 1
                    
                    current_sum = get_square_sum(r1, c1, r2, c2)
                    if current_sum <= threshold:
                        return True
            return False

        # Binary search for the maximum possible side length k
        # Possible side lengths range from 0 to min(m, n)
        low = 0
        high = min(m, n)
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid       # mid is a possible answer, try for a larger one
                low = mid + 1
            else:
                high = mid - 1  # mid is too large, try a smaller one
        
        return ans