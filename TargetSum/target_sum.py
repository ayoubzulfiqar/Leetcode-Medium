class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)

        # The problem can be transformed into a subset sum problem.
        # Let P be the sum of numbers chosen with '+' sign.
        # Let N be the sum of numbers chosen with '-' sign.
        # We want P - N = target.
        # We also know P + N = total_sum (sum of all numbers in nums).
        # Adding the two equations: 2P = target + total_sum
        # So, P = (target + total_sum) / 2.
        # This means we need to find the number of subsets of `nums` that sum up to P.

        # Conditions for a valid P:
        # 1. (target + total_sum) must be non-negative (since P, a sum of non-negative numbers, cannot be negative).
        #    This is equivalent to target >= -total_sum.
        #    Combined with the implicit condition P <= total_sum (which means target <= total_sum),
        #    it implies abs(target) <= total_sum.
        # 2. (target + total_sum) must be even (since P must be an integer).
        
        if (target + total_sum) % 2 != 0 or abs(target) > total_sum:
            return 0
        
        # The target sum for the subset sum problem
        subset_sum_target = (target + total_sum) // 2

        # dp[i] will store the number of ways to achieve sum i
        # Initialize dp array with size subset_sum_target + 1
        dp = [0] * (subset_sum_target + 1)
        
        # Base case: There is one way to achieve sum 0 (by choosing an empty set)
        dp[0] = 1

        # Iterate through each number in nums
        for num in nums:
            # Iterate backwards from subset_sum_target down to num
            # This ensures that each number is used at most once in forming a sum
            # (i.e., it's a 0/1 knapsack type of DP, not unbounded knapsack).
            # If num is 0, dp[j] += dp[j-0] means dp[j] += dp[j], effectively doubling it.
            # This correctly accounts for the two ways to use 0 (+0 or -0)
            # for any sum j that was already achievable.
            for j in range(subset_sum_target, num - 1, -1):
                dp[j] += dp[j - num]
        
        # The result is the number of ways to achieve subset_sum_target
        return dp[subset_sum_target]

```