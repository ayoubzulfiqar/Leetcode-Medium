class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        
        current_sum = sum(nums)
        
        # Iterate from the largest element downwards
        # i represents the index of the potential longest side.
        # The elements considered for the polygon are nums[0] through nums[i].
        # The number of sides considered is (i + 1).
        # A polygon must have at least 3 sides, so (i + 1) must be >= 3, which means i must be >= 2.
        # The loop range (len(nums) - 1, 1, -1) ensures i goes from len(nums) - 1 down to 2 (inclusive).
        for i in range(len(nums) - 1, 1, -1):
            # nums[i] is the current largest side in the current set of considered sides.
            # current_sum holds the sum of all sides from nums[0] to nums[i].
            # The sum of the other sides (excluding nums[i]) is current_sum - nums[i].
            if current_sum - nums[i] > nums[i]:
                # If the sum of the other sides is strictly greater than the longest side,
                # a valid polygon can be formed.
                # Since we are iterating from the largest possible sets of sides downwards,
                # this current_sum is the largest possible perimeter.
                return current_sum
            else:
                # If a valid polygon cannot be formed with nums[i] as the longest side,
                # then nums[i] cannot be part of any polygon that includes all elements
                # from nums[0] to nums[i].
                # We remove nums[i] from consideration for the next iteration by subtracting it
                # from current_sum. The next iteration will consider nums[0] to nums[i-1].
                current_sum -= nums[i]
        
        # If the loop completes, it means no valid polygon with at least 3 sides
        # could be formed from any subset of the given numbers following the greedy strategy.
        return -1