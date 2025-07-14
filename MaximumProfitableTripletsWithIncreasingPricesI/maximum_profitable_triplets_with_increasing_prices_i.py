class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 3:
            return 0

        # left_smaller[j] stores the maximum value prices[i] such that i < j and prices[i] < prices[j].
        # Initialize with -1 to indicate no such element found.
        left_smaller = [-1] * n

        # right_greater[j] stores the maximum value prices[k] such that k > j and prices[k] > prices[j].
        # Initialize with -1 to indicate no such element found.
        right_greater = [-1] * n

        # Populate left_smaller array
        # For each prices[j], find the maximum prices[i] to its left that is smaller than prices[j].
        for j in range(1, n):
            max_val_left = -1
            for i in range(j):
                if prices[i] < prices[j]:
                    max_val_left = max(max_val_left, prices[i])
            left_smaller[j] = max_val_left

        # Populate right_greater array
        # For each prices[j], find the maximum prices[k] to its right that is greater than prices[j].
        # Iterate j from right to left.
        for j in range(n - 2, -1, -1): # Loop from n-2 down to 0
            max_val_right = -1
            for k in range(j + 1, n):
                if prices[k] > prices[j]:
                    max_val_right = max(max_val_right, prices[k])
            right_greater[j] = max_val_right
        
        # Calculate the maximum profitable triplet sum
        # Initialize max_total_sum to 0. This assumes that if no valid triplet can be formed,
        # or if all valid triplets yield a non-positive sum, the answer is 0.
        max_total_sum = 0
        for j in range(n):
            # A valid triplet (i, j, k) exists if we found a suitable left_smaller and right_greater for prices[j].
            if left_smaller[j] != -1 and right_greater[j] != -1:
                current_triplet_sum = left_smaller[j] + prices[j] + right_greater[j]
                max_total_sum = max(max_total_sum, current_triplet_sum)
            
        return max_total_sum