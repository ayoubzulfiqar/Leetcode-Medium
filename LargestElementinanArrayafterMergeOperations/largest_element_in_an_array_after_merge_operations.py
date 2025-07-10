class Solution:
    def largestElementAfterMergeOperations(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Initialize current_sum with the last element.
        # This element is always part of the first potential sum segment
        # when processing from right to left.
        current_sum = nums[n - 1]
        
        # Initialize max_val with the last element.
        # This covers the case where no merges are possible or only the last element is the largest.
        max_val = current_sum

        # Iterate from the second-to-last element down to the first element.
        for i in range(n - 2, -1, -1):
            # If the current element (nums[i]) is less than or equal to the current_sum
            # (which represents the sum of elements to its right that have been merged),
            # then we can merge nums[i] into current_sum.
            if nums[i] <= current_sum:
                current_sum += nums[i]
            # If nums[i] is greater than current_sum, we cannot merge it.
            # This means the current_sum segment has ended, and its value is a candidate for max_val.
            # Then, nums[i] starts a new potential sum segment.
            else:
                max_val = max(max_val, current_sum)
                current_sum = nums[i]
        
        # After the loop, the final current_sum accumulated from the leftmost elements
        # is also a candidate for the maximum value.
        max_val = max(max_val, current_sum)
        
        return max_val