class Solution:
    def maxSumAfterOperation(self, nums: list[int]) -> int:
        n = len(nums)
        
        # prev_no_op: maximum subarray sum ending at previous index without any operation
        # prev_one_op: maximum subarray sum ending at previous index with exactly one operation
        
        # Initialize for the first element (index 0)
        prev_no_op = nums[0]
        prev_one_op = nums[0] * nums[0]
        
        # The overall maximum must come from a subarray where one operation was performed.
        # Initialize with the sum from the first element after operation.
        overall_max_sum = prev_one_op
        
        # Iterate from the second element
        for i in range(1, n):
            num = nums[i]
            
            # Calculate current_no_op: maximum subarray sum ending at current index 'i' without any operation
            # It's either starting a new subarray with 'num', or extending the previous no-op subarray.
            current_no_op = max(num, prev_no_op + num)
            
            # Calculate current_one_op: maximum subarray sum ending at current index 'i' with exactly one operation
            # There are three possibilities:
            # 1. The current 'num' is squared, forming a new subarray: num * num
            # 2. The current 'num' is squared, extending a previous no-op subarray: prev_no_op + num * num
            # 3. An element before 'num' was squared, and 'num' extends that one-op subarray: prev_one_op + num
            current_one_op = max(num * num, prev_no_op + num * num, prev_one_op + num)
            
            # Update the overall maximum sum found so far, considering only subarrays with one operation.
            overall_max_sum = max(overall_max_sum, current_one_op)
            
            # Prepare for the next iteration by updating previous values
            prev_no_op = current_no_op
            prev_one_op = current_one_op
            
        return overall_max_sum

```