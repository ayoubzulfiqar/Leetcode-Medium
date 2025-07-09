class Solution:
    def maxAlternatingSubarraySum(self, nums: list[int]) -> int:
        def get_sign(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0

        if not nums:
            return 0 # Or handle as per specific problem constraints for empty input

        max_so_far = nums[0]
        current_max = nums[0]

        for i in range(1, len(nums)):
            sign_prev = get_sign(nums[i-1])
            sign_curr = get_sign(nums[i])

            # Check if the current element and the previous element form an alternating pair
            # This means both must be non-zero and have different signs.
            if sign_prev != 0 and sign_curr != 0 and sign_prev != sign_curr:
                current_max += nums[i]
            else:
                # If they do not alternate, or if either is zero,
                # the alternating sequence is broken. Start a new sequence
                # from the current element.
                current_max = nums[i]
            
            # Update the overall maximum sum found so far
            max_so_far = max(max_so_far, current_max)
        
        return max_so_far