class Solution:
    def maximumSumOfHeights(self, heights: list[int]) -> int:
        n = len(heights)
        max_total_sum = 0

        for p in range(n):  # Iterate through each possible peak index
            current_sum = heights[p]  # The peak itself contributes its original height

            # Calculate heights and sum for the left side (non-decreasing towards peak)
            # The height of the current tower must be <= the previous tower (closer to peak)
            # and <= its original height. To maximize sum, we take the minimum.
            left_height = heights[p]
            for i in range(p - 1, -1, -1):
                left_height = min(left_height, heights[i])
                current_sum += left_height

            # Calculate heights and sum for the right side (non-increasing away from peak)
            # The height of the current tower must be <= the previous tower (closer to peak)
            # and <= its original height. To maximize sum, we take the minimum.
            right_height = heights[p]
            for i in range(p + 1, n):
                right_height = min(right_height, heights[i])
                current_sum += right_height
            
            max_total_sum = max(max_total_sum, current_sum)
        
        return max_total_sum