class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Find the index of the minimum element (first occurrence)
        min_idx = 0
        for i in range(1, n):
            if nums[i] < nums[min_idx]:
                min_idx = i

        # Find the index of the maximum element (last occurrence)
        max_idx = 0
        for i in range(1, n):
            if nums[i] >= nums[max_idx]: # Use >= to get the last occurrence
                max_idx = i

        # Calculate swaps for minimum element to move to the beginning
        # This is simply its current index, as each swap moves it one step left.
        swaps = min_idx

        # Calculate swaps for maximum element to move to the end
        # This is (n - 1) - max_idx, as each swap moves it one step right.
        # If the minimum element was originally to the right of the maximum element,
        # moving the minimum element to the front will shift the maximum element's
        # effective index one position to the left. This means the maximum element
        # is now one step closer to the end, reducing its required swaps by 1.
        if min_idx < max_idx:
            # min_idx is to the left of max_idx, no effective shift for max_idx
            swaps += (n - 1) - max_idx
        else: # min_idx > max_idx
            # min_idx is to the right of max_idx, max_idx effectively shifts left by 1
            swaps += (n - 1) - max_idx - 1

        return swaps

```