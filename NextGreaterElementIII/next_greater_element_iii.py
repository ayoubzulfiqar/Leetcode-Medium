class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))

        i = len(s) - 2
        while i >= 0 and s[i] >= s[i+1]:
            i -= 1

        if i < 0:
            return -1

        j = len(s) - 1
        while j > i and s[j] <= s[i]:
            j -= 1

        s[i], s[j] = s[j], s[i]

        left = i + 1
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        result = int("".join(s))

        if result > 2**31 - 1:
            return -1
        else:
            return result