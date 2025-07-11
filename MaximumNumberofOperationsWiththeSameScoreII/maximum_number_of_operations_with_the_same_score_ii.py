class Solution:
    def maxOperations(self, nums: list[int]) -> int:
        n = len(nums)
        
        def calculate_max_ops(target_score: int) -> int:
            memo = {}

            def dp(left: int, right: int) -> int:
                if left >= right:
                    return 0
                if (left, right) in memo:
                    return memo[(left, right)]

                max_current_ops = 0

                # Option 1: Delete first two elements (nums[left] and nums[left+1])
                # Check if there are at least two elements remaining and their sum matches the target
                if left + 1 <= right and nums[left] + nums[left+1] == target_score:
                    max_current_ops = max(max_current_ops, 1 + dp(left + 2, right))

                # Option 2: Delete last two elements (nums[right-1] and nums[right])
                # Check if there are at least two elements remaining and their sum matches the target
                if right - 1 >= left and nums[right-1] + nums[right] == target_score:
                    max_current_ops = max(max_current_ops, 1 + dp(left, right - 2))

                # Option 3: Delete first and last elements (nums[left] and nums[right])
                # Check if there are at least two elements remaining and their sum matches the target
                if nums[left] + nums[right] == target_score:
                    max_current_ops = max(max_current_ops, 1 + dp(left + 1, right - 1))
                
                memo[(left, right)] = max_current_ops
                return max_current_ops

            return dp(0, n - 1)

        ans = 0

        # The target score must be one of the scores from the initial possible operations.
        # Since n >= 2, all these initial operations are always possible.

        # Case 1: Assume the target score is nums[0] + nums[1]
        ans = max(ans, calculate_max_ops(nums[0] + nums[1]))

        # Case 2: Assume the target score is nums[n-1] + nums[n-2]
        ans = max(ans, calculate_max_ops(nums[n-1] + nums[n-2]))

        # Case 3: Assume the target score is nums[0] + nums[n-1]
        ans = max(ans, calculate_max_ops(nums[0] + nums[n-1]))
        
        return ans

```