class Solution:
    def minOperations(self, k: int) -> int:
        if k == 1:
            return 0

        min_ops = float('inf')

        for x in range(1, k + 1):
            m = (k + x - 1) // x
            current_ops = (x - 1) + (m - 1)
            min_ops = min(min_ops, current_ops)

        return min_ops