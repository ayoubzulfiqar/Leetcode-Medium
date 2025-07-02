class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        remaining = n
        step = 1
        direction = True  # True for left-to-right, False for right-to-left

        while remaining > 1:
            if direction:  # Left-to-right pass
                head += step
            else:  # Right-to-left pass
                # Head changes if remaining count is odd (first element is removed)
                # or if it's the first right-to-left pass (which implies remaining is odd after L-R pass)
                # A simpler way to put it: head changes if it's a left-to-right pass,
                # or if it's a right-to-left pass AND the number of remaining elements is odd.
                if remaining % 2 == 1:
                    head += step
            
            remaining //= 2
            step *= 2
            direction = not direction
            
        return head