class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)

        def count_less_equal(val: int) -> int:
            count = 0
            row = n - 1
            col = 0

            while row >= 0 and col < n:
                if matrix[row][col] <= val:
                    count += (row + 1)
                    col += 1
                else:
                    row -= 1
            return count

        low = matrix[0][0]
        high = matrix[n - 1][n - 1]
        ans = high

        while low <= high:
            mid = low + (high - low) // 2
            
            count = count_less_equal(mid)

            if count >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans