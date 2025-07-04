class Solution:
    def getStrongest(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)

        # 1. Find the center 'm'
        # Sort a copy of the array to find the median value.
        # The problem defines the center as the element at position ((n - 1) / 2)
        # in the sorted list (0-indexed).
        sorted_arr = sorted(arr)
        m_index = (n - 1) // 2
        m = sorted_arr[m_index]

        # 2. Sort the original array based on the "strength" definition.
        # A value arr[i] is stronger than arr[j] if |arr[i] - m| > |arr[j] - m|.
        # If |arr[i] - m| == |arr[j] - m|, then arr[i] is stronger than arr[j] if arr[i] > arr[j].
        #
        # To achieve this custom sorting order using Python's default ascending sort:
        # - We want larger |arr[i] - m| to come first, so we negate abs(x - m).
        # - If |arr[i] - m| are equal, we want larger arr[i] to come first, so we negate x.
        # The key for sorting will be a tuple: (-abs(x - m), -x).
        arr.sort(key=lambda x: (-abs(x - m), -x))

        # 3. Return the k strongest values.
        # These will be the first k elements after sorting.
        return arr[:k]