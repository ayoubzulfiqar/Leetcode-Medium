class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        max_len = 0
        i = 0
        while i < n:
            base = i

            while i + 1 < n and arr[i] < arr[i+1]:
                i += 1

            peak_idx = i

            if i == base:
                i += 1
                continue

            while i + 1 < n and arr[i] > arr[i+1]:
                i += 1

            if i == peak_idx:
                i += 1
                continue

            max_len = max(max_len, i - base + 1)

        return max_len