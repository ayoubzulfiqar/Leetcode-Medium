class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        min_val = float('inf')
        max_val = float('-inf')
        min_idx = -1
        max_idx = -1

        for i in range(n):
            if nums[i] < min_val:
                min_val = nums[i]
                min_idx = i
            if nums[i] > max_val:
                max_val = nums[i]
                max_idx = i

        # Determine which index is closer to the front (idx1) and which is closer to the back (idx2)
        idx1 = min(min_idx, max_idx)
        idx2 = max(min_idx, max_idx)

        # Option 1: Remove both elements by deleting from the front
        # We need to remove all elements up to and including the rightmost of the two (idx2)
        # Number of deletions: (idx2 - 0) + 1 = idx2 + 1
        cost1 = idx2 + 1

        # Option 2: Remove both elements by deleting from the back
        # We need to remove all elements from the leftmost of the two (idx1) to the end
        # Number of deletions: (n - 1 - idx1) + 1 = n - idx1
        cost2 = n - idx1

        # Option 3: Remove one element from the front and the other from the back
        # To remove idx1 from front: (idx1 - 0) + 1 = idx1 + 1 deletions
        # To remove idx2 from back: (n - 1 - idx2) + 1 = n - idx2 deletions
        # Total deletions: (idx1 + 1) + (n - idx2)
        cost3 = (idx1 + 1) + (n - idx2)

        return min(cost1, cost2, cost3)