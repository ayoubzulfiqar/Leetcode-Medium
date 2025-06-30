from typing import List

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        def reverse_sub_array(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        n = len(s)
        if n == 0:
            return

        reverse_sub_array(s, 0, n - 1)

        start = 0
        for end in range(n + 1):
            if end == n or s[end] == ' ':
                reverse_sub_array(s, start, end - 1)
                start = end + 1