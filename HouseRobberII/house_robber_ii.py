class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob_linear(arr: list[int]) -> int:
            """
            Helper function to solve the classic House Robber problem (linear arrangement).
            Calculates the maximum amount of money that can be robbed from a linear
            sequence of houses without robbing adjacent ones.
            Uses O(1) space dynamic programming.
            """
            if not arr:
                return 0
            
            # dp_i_minus_2 represents the maximum money robbed up to house i-2
            # dp_i_minus_1 represents the maximum money robbed up to house i-1
            dp_i_minus_2 = 0
            dp_i_minus_1 = 0

            for num in arr:
                # The maximum money up to the current house (num) is either:
                # 1. Not robbing the current house, so it's the same as dp_i_minus_1.
                # 2. Robbing the current house, so it's num + dp_i_minus_2 (since we can't rob dp_i_minus_1).
                current_max = max(dp_i_minus_1, dp_i_minus_2 + num)
                
                # Update for the next iteration
                dp_i_minus_2 = dp_i_minus_1
                dp_i_minus_1 = current_max
            
            return dp_i_minus_1

        # Case 1: Exclude the last house (nums[n-1]). This allows robbing the first house.
        # We consider houses from index 0 to n-2.
        max_money_case1 = rob_linear(nums[0:n-1])

        # Case 2: Exclude the first house (nums[0]). This allows robbing the last house.
        # We consider houses from index 1 to n-1.
        max_money_case2 = rob_linear(nums[1:n])

        # The maximum money that can be robbed is the maximum of these two cases.
        return max(max_money_case1, max_money_case2)