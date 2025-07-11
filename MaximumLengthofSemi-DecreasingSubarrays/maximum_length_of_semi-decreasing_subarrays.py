def max_length_semi_decreasing_subarrays(nums):
    """
    Calculates the maximum length of a semi-decreasing subarray.
    A semi-decreasing subarray is defined as a subarray where each element
    is less than or equal to the preceding element (i.e., non-increasing).

    Args:
        nums: A list of integers.

    Returns:
        An integer representing the maximum length of a semi-decreasing subarray.
        Returns 0 if the input list is empty.
    """
    if not nums:
        return 0

    max_len = 1  # A single element is always a semi-decreasing subarray
    current_len = 1

    for i in range(1, len(nums)):
        if nums[i-1] >= nums[i]:
            # The current element maintains the non-increasing property
            current_len += 1
        else:
            # The non-increasing sequence is broken, reset current_len
            # The current element itself starts a new potential sequence of length 1
            current_len = 1

        # Update the maximum length found so far
        max_len = max(max_len, current_len)

    return max_len