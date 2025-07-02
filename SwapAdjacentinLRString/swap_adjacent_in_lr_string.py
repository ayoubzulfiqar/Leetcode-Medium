class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        n = len(start)

        p1 = 0  # Pointer for start string
        p2 = 0  # Pointer for result string

        while p1 < n and p2 < n:
            # Advance p1 past 'X' characters in start
            while p