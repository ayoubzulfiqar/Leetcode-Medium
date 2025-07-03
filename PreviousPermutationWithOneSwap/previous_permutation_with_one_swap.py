class Solution:
    def prevPermOpt1(self, arr: list[int]) -> list[int]:
        n = len(arr)

        # Step 1: Find the largest index i such that arr[i] > arr[i+1]
        # Iterate from right to left (n-2 down to 0)
        i = n - 2
        while i >= 0 and arr[i] <= arr[i+1]:
            i -= 1

        # If no such index i exists, the array is already sorted in non-decreasing order.
        # This means it's the smallest possible permutation, and no smaller one
        # can be made with a single swap. Return the original array.
        if i == -1:
            return arr

        # Step 2: Find the largest index j > i such that arr[j] < arr[i].
        # Among such arr[j], we want the one with the largest value.
        # If there are multiple such arr[j] with the same largest value,
        # we pick the one with the largest index (rightmost).
        
        best_j = -1
        max_val_for_swap = -1

        # Iterate from left to right in the suffix arr[i+1:]
        for k in range(i + 1, n):
            if arr[k] < arr[i]:
                if arr[k] > max_val_for_swap:
                    max_val_for_swap = arr[k]
                    best_j = k
                elif arr[k] == max_val_for_swap:
                    # If values are equal, pick the one with the larger index (rightmost)
                    best_j = k
        
        # Step 3: Swap arr[i] and arr[best_j]
        # A suitable best_j is guaranteed to be found because if 'i' was found,
        # it means arr[i] > arr[i+1], implying arr[i+1] is a candidate for arr[j].
        arr[i], arr[best_j] = arr[best_j], arr[i]

        return arr