```python
class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        n = len(arr)
        result = []

        def _flip(sub_arr, k):
            # Reverses the first k elements of sub_arr.
            # k is 1-indexed, so it reverses sub_arr[0] up to sub_arr[k-1].
            sub_arr[:k] = sub_arr[:k][::-1]

        # Iterate from the largest element (n) down to 1.
        # In each iteration, we place the current_max_val into its correct sorted position
        # at the end of the current unsorted prefix.
        for current_max_val in range(n, 0, -1):
            # Find the index of the current_max_val within the unsorted part of the array.
            # The unsorted part is arr[0...current_max_val-1].
            idx_of_max = -1
            for i in range(current_max_val):
                if arr[i] == current_max_val:
                    idx_of_max = i
                    break
            
            # If current_max_val is already in its correct final sorted position for this step, skip.
            # This means it's at arr[current_max_val - 1].
            if idx_of_max == current_max_val - 1:
                continue

            # Step 1: Bring the current_max_val to the front (index 0).
            # This is done by flipping the prefix up to its current position.
            # Only perform this flip if it's not already at the front.
            if idx_of_max != 0:
                _flip(arr, idx_of_max + 1)
                result.append(idx_of_max + 1)
            
            # Step 2: Bring the current_max_val from the front to its correct sorted position.
            # This position is at the end of the current unsorted prefix (index current_max_val - 1).
            # This is done by flipping the entire current unsorted prefix.
            _flip(arr, current_max_val)
            result.append(current_max_val)
            
        return result

```