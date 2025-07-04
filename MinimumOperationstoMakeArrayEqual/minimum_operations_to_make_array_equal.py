class Solution:
    def minOperations(self, n: int) -> int:
        m = n // 2
        if n % 2 == 0:
            return m * m
        else:
            return m * (m + 1)