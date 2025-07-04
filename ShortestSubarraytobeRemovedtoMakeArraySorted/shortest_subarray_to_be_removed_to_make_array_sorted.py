class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        n = len(arr)

        # 1. Find the longest non-decreasing prefix
        # 'left' will be the index of the last element of the longest non-decreasing prefix
        # arr[0...left] is non-decreasing
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        # If the entire array is already sorted, no removal is needed
        if left == n - 1:
            return 0

        # 2. Find the longest non-decreasing suffix
        # 'right' will be the index of the first element of the longest non-decreasing suffix
        # arr[right...n-1] is non-decreasing
        right = n - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        # Initial minimum length of subarray to remove:
        # Option A: Remove arr[left+1 ... n-1] (keep only the prefix arr[0...left])
        # Length to remove: n - (left + 1)
        # Option B: Remove arr[0 ... right-1] (keep only the suffix arr[right...n-1])
        # Length to remove: right
        ans = min(n - (left + 1), right)

        # 3. Explore combinations of prefix arr[0...i] and suffix arr[j...n-1]
        # where arr[i] <= arr[j] and i < j.
        # We iterate 'i' from the start of the array up to 'left' (inclusive),
        # ensuring arr[0...i] is a valid non-decreasing prefix.
        # We use a two-pointer 'j' starting from 'right' to find the smallest 'j'
        # such that arr[j...n-1] is a valid non-decreasing suffix and arr[i] <= arr[j].
        j = right
        for i in range(left + 1): # i iterates from 0 to left
            # Move 'j' forward as long as arr[i] is greater than arr[j]
            # and 'j' is within bounds.
            while j < n and arr[i] > arr[j]:
                j += 1

            # If 'j' reaches the end of the array, it means arr[i] is too large
            # to be combined with any element from the suffix arr[right...n-1].
            # Since arr[i] is non-decreasing as 'i' increases, further 'i' values
            # will also be too large, so we can break.
            if j == n:
                break

            # We found a valid combination: arr[0...i] and arr[j...n-1]
            # The subarray to remove is arr[i+1 ... j-1].
            # Its length is (j - 1) - (i + 1) + 1 = j - i - 1.
            ans = min(ans, j - i - 1)

        return ans