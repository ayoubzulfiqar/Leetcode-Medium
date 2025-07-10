import math

class Solution:
    def minSpaceWastedKResizing(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # dp[i][j] stores the minimum total space wasted for the first i elements (nums[0]...nums[i-1])
        # using exactly j resizing operations.
        # Initialize with infinity.
        dp = [[math.inf] * (k + 1) for _ in range(n + 1)]

        # Base case: 0 elements, 0 resizes, 0 wasted space.
        dp[0][0] = 0

        # Iterate through the number of elements considered (from 1 to n)
        for i in range(1, n + 1):
            # Iterate through the number of allowed resizes (from 0 to k)
            for j in range(k + 1):
                current_max = 0
                current_sum = 0
                
                # Iterate backwards from i-1 down to 0 to define the start of the last segment.
                # 'p' is the 0-indexed start of the current segment (nums[p]...nums[i-1]).
                for p in range(i - 1, -1, -1):
                    current_max = max(current_max, nums[p])
                    current_sum += nums[p]
                    
                    # Calculate the space wasted for this specific segment.
                    # The array size for this segment is current_max.
                    # The number of elements in this segment is (i - p).
                    segment_wasted = current_max * (i - p) - current_sum

                    # If this segment starts from index 0 (p == 0), it means the entire prefix nums[0]...nums[i-1]
                    # is covered by a single array size (the initial size).
                    # In this case, no resizing operations are counted for this segment.
                    if p == 0:
                        if j == 0:  # This path is only valid if exactly 0 resizes are used.
                            dp[i][j] = min(dp[i][j], segment_wasted)
                    # If this segment starts from an index p > 0, it means a resize operation occurred at index p-1.
                    # The previous state would be dp[p][j-1], representing the minimum wasted space for nums[0]...nums[p-1]
                    # using one less resize operation.
                    else:
                        if j > 0 and dp[p][j - 1] != math.inf:
                            dp[i][j] = min(dp[i][j], dp[p][j - 1] + segment_wasted)
        
        # The problem asks for the minimum total space wasted if we can resize the array at most k times.
        # This means we need to find the minimum value among all dp[n][j] where j is from 0 to k.
        return min(dp[n][j] for j in range(k + 1))

```