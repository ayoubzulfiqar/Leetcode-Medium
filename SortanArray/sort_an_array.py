class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # Build max-heap (rearrange array)
        # Start from the last non-leaf node and go up to the root
        # The loop runs from (n//2 - 1) down to 0
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(nums, n, i)

        # One by one extract elements from the heap
        # The loop runs from (n - 1) down to 1
        for i in range(n - 1, 0, -1):
            # Move current root (largest element) to end of the array
            nums[i], nums[0] = nums[0], nums[i]
            # Call max heapify on the reduced heap (size i)
            self._heapify(nums, i, 0)
        
        return nums

    def _heapify(self, arr: list[int], n: int, i: int):
        largest = i  # Initialize largest as root
        left = 2 * i + 1  # left child index
        right = 2 * i + 2  # right child index

        # If left child exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # If right child exists and is greater than current largest
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not root
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap

            # Recursively heapify the affected sub-tree
            self._heapify(arr, n, largest)