import bisect

class Solution:
    def findMedian(self, matrix: list[list[int]]) -> int:
        R = len(matrix)
        C = len(matrix[0])

        total_elements = R * C
        
        # The median position (1-indexed) for a set of N elements is (N + 1) // 2.
        # This approach finds the (total_elements + 1) // 2 -th smallest element.
        k = (total_elements + 1) // 2

        # Initialize the search range for the median value.
        # The minimum possible value for the median is the smallest element in the matrix.
        # The maximum possible value for the median is the largest element in the matrix.
        low = float('inf')
        high = float('-inf')

        for r in range(R):
            low = min(low, matrix[r][0])
            high = max(high, matrix[r][C-1])
        
        ans = -1

        # Perform binary search on the possible values of the median.
        while low <= high:
            mid = low + (high - low) // 2
            
            count_le_mid = 0 # Count of elements less than or equal to 'mid'
            
            # For each row, count elements <= mid using bisect_right.
            # bisect_right returns an insertion point which also corresponds to
            # the count of elements less than or equal to the given value in a sorted list.
            for r in range(R):
                count_le_mid += bisect.bisect_right(matrix[r], mid)
            
            if count_le_mid < k:
                # If the count of elements <= mid is less than k, it means 'mid' is too small.
                # The actual median must be greater than 'mid'.
                low = mid + 1
            else:
                # If the count of elements <= mid is greater than or equal to k,
                # 'mid' could be the median, or the median is even smaller.
                # We store 'mid' as a potential answer and try to find a smaller one.
                ans = mid
                high = mid - 1
                
        return ans