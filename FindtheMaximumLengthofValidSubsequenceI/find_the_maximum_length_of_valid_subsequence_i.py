class Solution:
    def longestValidSubsequence(self, nums: list[int]) -> int:
        count_odd = 0
        count_even = 0

        # dp_odd: length of the longest alternating subsequence ending with an odd number
        # dp_even: length of the longest alternating subsequence ending with an even number
        dp_odd = 0
        dp_even = 0

        for num in nums:
            if num % 2 == 0:  # Current number is even
                count_even += 1
                # To form an alternating subsequence ending with an even number,
                # the previous number in the subsequence must have been odd.
                # So, we extend a subsequence that ended with an odd number.
                # If dp_odd is 0, it means no odd numbers have been encountered yet,
                # so this even number starts a new subsequence of length 1.
                # (dp_odd + 1 correctly handles this: 0 + 1 = 1)
                dp_even = dp_odd + 1
            else:  # Current number is odd
                count_odd += 1
                # To form an alternating subsequence ending with an odd number,
                # the previous number in the subsequence must have been even.
                # So, we extend a subsequence that ended with an even number.
                # If dp_even is 0, this odd number starts a new subsequence of length 1.
                # (dp_even + 1 correctly handles this: 0 + 1 = 1)
                dp_odd = dp_even + 1
        
        # Case 1: The valid subsequence has all adjacent pairs summing to an even number.
        # This implies all numbers in the subsequence must have the same parity (all odd or all even).
        # The longest such subsequence is simply the count of the more frequent parity in the original array.
        max_same_parity_subsequence = max(count_odd, count_even)

        # Case 2: The valid subsequence has all adjacent pairs summing to an odd number.
        # This implies numbers in the subsequence must alternate parity (e.g., odd, even, odd, ... or even, odd, even, ...).
        # The length of the longest such subsequence is found using the dp_odd and dp_even states.
        max_alternating_parity_subsequence = max(dp_odd, dp_even)

        # The overall maximum length is the maximum of the lengths found in Case 1 and Case 2.
        return max(max_same_parity_subsequence, max_alternating_parity_subsequence)

```